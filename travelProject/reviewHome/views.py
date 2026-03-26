from django.shortcuts import render

# Create your views here.
def reviewHome(request):
    return render(request, "blog-home.html")