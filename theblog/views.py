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

  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context["cat_menu"] = cat_menu
    return context

def CategoryListView(request):
  cat_menu_list = Category.objects.all()

  return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def CategoryView(request, cats):
  category_posts = Post.objects.filter(category=cats.replace('-', ' '))
  cat_menu = Category.objects.all()

  return render(request, 'categories.html', {"cats": cats.title().replace('-', ' '), "category_posts": category_posts, "cat_menu": cat_menu })

class ArticleDetailView(DetailView):
  model = Post
  template_name = "article_details.html"

  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
    context["cat_menu"] = cat_menu
    return context

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