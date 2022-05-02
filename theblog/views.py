from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from theblog.models import Post
from .forms import PostForm, EditPostForm

# Create your views here.
class HomeView(ListView):
  model = Post
  template_name = "home.html"

class ArticleDetailView(DetailView):
  model = Post
  template_name = "article_details.html"

class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = "add_post.html"
  # fields = '__all__' # put all fields
  # fields = ('title', 'body')

class UpdatePostView(UpdateView):
  model = Post
  template_name = "update_post.html"
  form_class = EditPostForm
  # fields = ['title', 'title_tag', 'body']