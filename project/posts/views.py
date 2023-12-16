from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPost

def index(request):
    posts = Post.objects.all()
    return render(request, 'post/posts.html', context={'posts':posts})

def create(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Post.objects.create(category_id=category, text=text, title=title)
            return redirect('home')

    form = AddPost ()
    return render (request, 'post/create.html', context={'form': form})


def update(request, id):
    try:
        post = Post.objects.get(id=id)
        print(post)
        if request.method == 'POST':
            post.category = request.POST.get('category')
            post.title = request.POST.get('title')
            post.text = request.POST.get ('text')
            post.save()
            return redirect('home')
        else:
            return render(request, 'post/update.html', context={'post': post})
    except:
        return redirect('create')

def delete(request, id):
    try:
        post = Post.objects.get (id=id)
        post.delete ()
        return redirect ('home')
    except:
        return redirect ('home')

def category(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            Post.objects.create(category_id=category)
            return redirect('home')

    form = AddPost()
    return render (request, 'create.html', context={'form': form})