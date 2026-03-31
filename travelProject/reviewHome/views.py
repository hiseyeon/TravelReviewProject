from django.shortcuts import render, redirect, get_object_or_404 
from travel.models import Review
from travel.forms import ReviewModelForm

# Create your views here.
def reviewHome(request):
    return render(request, "blog-home.html")

def blog_list(request):
    review = Review.objects.all().order_by('-created_at')
    return render(request, "blog_list.html", {"review" : review})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Review, pk=blog_id)
    return render(request, "blog_detail.html", {"review": blog})


def blog_update(request, id):
    review = get_object_or_404(Review, pk=id) 

    if request.method == 'POST':
        form = ReviewModelForm(request.POST, instance=review) 
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