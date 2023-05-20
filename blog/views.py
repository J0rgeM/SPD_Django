from django.views import generic
from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

@csrf_protect
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')  # Replace 'post_detail' with your desired post detail view name
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
