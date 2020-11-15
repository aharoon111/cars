from django.shortcuts import render
from .models import Post 

# Create your views here.



def post_list(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'all_posts':all_posts})



def single_post(request,id):
    post_detail = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'single_post':post_detail})