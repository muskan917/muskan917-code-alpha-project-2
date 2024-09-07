from django.shortcuts import render, redirect
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post-list')

def add_comment(request, post_id):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(user=request.user, post=post, comment=comment_text)
        return redirect('post-list')
