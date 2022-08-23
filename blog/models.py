from django.db import models

# Create your models here.
class DatabaseBlog(models.Model):
    blog_id = models.AutoField
    BlogTitle = models.CharField(max_length=30,default="Enter the Title of Blog")
    BlogDate = models.DateTimeField(auto_now_add=True)
    BlogMoral = models.CharField(max_length=50,default="Enter the Moral Of the Blog")
    BlogDetails = models.CharField(max_length=5000,default="Write Complete Blog Here")
    BlogAuthor = models.CharField(max_length=20,default="Name Of Blogger")
    BlogImage = models.ImageField(upload_to='shop/image', default="")

    def __str__(self):
        return self.BlogTitle

class PublishBlog(models.Model):
    publish_id= models.AutoField
    Author_Name = models.CharField(max_length=50)
    Blogger_Email = models.CharField(max_length=50)
    Blogger_Title = models.CharField(max_length=80)
    Blogger_Content = models.CharField(max_length=5000000)
    Blog_Image = models.ImageField(upload_to='shop/image',default='')
    Blog_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Blogger_Title