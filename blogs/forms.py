from django.forms import ModelForm
from blogs.models import *


class AddBlogForm(ModelForm):
    class Meta:
        model = BlogPosts
        fields = "__all__"
