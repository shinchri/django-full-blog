from django import forms

from .models import Post, Category

# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name')

# choice_list = []

# for item in choices:
#   choice_list.append(item)

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title...'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'elder', 'type':'hidden'}),
      #'author': forms.Select(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'snippet': forms.Textarea(attrs={'class': 'form-control'}),
    }

class EditPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'category', 'body', 'snippet')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title...'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'snippet': forms.Textarea(attrs={'class': 'form-control'}),
    }