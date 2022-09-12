from django.shortcuts import render
from django.views import *
from blogs.models import *

# view all blogs
class ViewAll(View):
    def get(self, request):
        bl = BlogPosts.objects.all()
        context = {
            "data": bl,
        }
        return render(request, "blogs/allblogs.html", context)


# view 1 blog based on id from query param
class ViewOne(View):
    def get(self, request):
        ind = request.GET.get("id")
        if ind:
            bl = BlogPosts.objects.get(id=ind)
            context = {
                "data": bl,
            }
        else:
            context = {
                "data": None,
            }
        return render(request, "blogs/oneblog.html", context)
