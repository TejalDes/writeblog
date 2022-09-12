from django.db import models


class Blogger(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)


class BlogPosts(models.Model):
    name = models.CharField(max_length=200)
    date_modified = models.DateField()
    date_created = models.DateField()
    blog_text = models.TextField()
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)


class Likes(models.Model):
    blogposts = models.ForeignKey(BlogPosts, on_delete=models.CASCADE)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)


class Comments(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    comment_text = models.TextField
    comment_date = models.DateField
