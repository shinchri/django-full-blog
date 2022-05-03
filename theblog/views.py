from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from theblog.models import Post, Category
from .forms import PostForm, EditPostForm

# Create your views here.
class HomeView(ListView):
  model = Post
  template_name = "home.html"
  ordering = ['-post_date', '-id']

def CategoryView(request, cats):
  category_posts = Post.objects.filter(category=cats.replace('-', ' '))

  return render(request, 'categories.html', {"cats": cats.title().replace('-', ' '), "category_posts": category_posts})

class ArticleDetailView(DetailView):
  model = Post
  template_name = "article_details.html"

class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = "add_post.html"
  # fields = '__all__' # put all fields
  # fields = ('title', 'body')

class AddCategoryView(CreateView):
  model = Category
  template_name = "add_category.html"
  fields = '__all__' # put all fields
  # fields = ('title', 'body')

class UpdatePostView(UpdateView):
  model = Post
  template_name = "update_post.html"
  form_class = EditPostForm
  # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
  model = Post
  template_name = "delete_post.html"
  success_url = reverse_lazy('home')