from django.shortcuts import render
from django.views import *
from blogs.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import AddBlogForm

# view all blogs
class ViewAll(ListView):
    model = BlogPosts
    template_name = "blogs/allblogs.html"


# view 1 blog based on id from query param
# class ViewOne(View):
#     def get(self, request):
#         ind = request.GET.get("id")
#         if ind:
#             bl = BlogPosts.objects.get(id=ind)
#             context = {
#                 "data": bl,
#             }
#         else:
#             context = {
#                 "data": None,
#             }
#         return render(request, "blogs/oneblog.html", context)


class ViewOne(DetailView):
    model = BlogPosts
    template_name = "blogs/oneblog.html"

    # override queryset func
    # this doesnt work for url parameters
    # it works only for urls.p hardcoded id
    # def get_queryset(self):
    #     ind = self.request.GET.get("id")
    #     print(ind)
    #     bl = BlogPosts.objects.get(id=ind)
    #     return bl

    # overriding get_object function instead
    def get_object(self):
        ind = self.request.GET.get("id")
        print(ind)
        bl = BlogPosts.objects.get(id=ind)
        return bl


def AddBlogView(request):
    context = {}

    # getting the form
    form = AddBlogForm(request.POST or None)

    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "blogs/blogposts_form.html", context)
