from django.shortcuts import render, redirect, get_object_or_404 
from travel.models import Review, Comment
from travel.forms import ReviewModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
def reviewHome(request):
    return render(request, "blog-home.html")

def blog_list(request):
    review = Review.objects.all().order_by('-created_at')
    my_paginator = Paginator(review, 5)
    page_num = request.GET.get('page')
    review = my_paginator.get_page(page_num)
    return render(request, "blog_list.html", {"review" : review})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Review, pk=blog_id)
    comment_form = CommentForm()
    context = {
        'review' : blog,
        'comment_form': comment_form
    }
    return render(request, 'blog_detail.html', context)


def blog_update(request, id):
    review = get_object_or_404(Review, pk=id) 

    if request.method == 'POST' or request.method == 'FILES':
        form = ReviewModelForm(request.POST, request.FILES, instance=review) 
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=review.id) 
    else:
        form = ReviewModelForm(instance=review)
    return render(request, 'form_create.html', {'form': form, 'blog_id': id})


def blog_delete(request, id):
    blog = Review.objects.get(pk=id)
    blog.delete()
    return redirect('blog_list')


# 댓글 작성
def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Review, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('blog_detail', id)

# 댓글 수정
def update_comment(request, blog_id, com_id):
    comment = Comment.objects.get(id=com_id)
	    
    if request.method == "POST": # 사용자가 수정 후 POST 요청을 보냈을 때
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('blog_detail', blog_id)
    else: # GET 요청일 때
        comment_form = CommentForm(instance=comment)
        context = {'comment_form' : comment_form}
        return render(request, 'comment_update.html', context)
    

# 댓글 삭제
def delete_comment(request, blog_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('blog_detail', blog_id)