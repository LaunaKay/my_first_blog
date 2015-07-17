from django.shortcuts import render
# import if using timezone
from django.utils import timezone
from .models import Post
#import 404 view
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
#set var equal to object or 404 page, matching on pk
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form=PostForm()
        return render(request, 'blog/post_edit.html', {'form':form})

