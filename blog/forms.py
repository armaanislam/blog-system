from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['host', 'reaction_count']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']