from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title',
        #           'content',
        #           'cont',
        #           'cont_up',
        #           'user',
        #           'category',
        #           ]
