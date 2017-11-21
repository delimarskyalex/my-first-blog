from django import forms
from .models import Post

class PostForm(Forms,ModelForm):
    class Meta:
        model = Post
        Fields = ('title','text',)
