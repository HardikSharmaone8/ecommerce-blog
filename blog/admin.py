from django.contrib import admin
from .models import DatabaseBlog,PublishBlog
# Register your models here.
admin.site.register(DatabaseBlog)
admin.site.register(PublishBlog)