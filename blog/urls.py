from django.urls import path
from .import views

urlpatterns=[
    path("content",views.show_blog,name='viewblogs'),
    path("contentdetails/<int:myid>",views.show_blog_details,name='viewblogs'),
    path("userContentDetails/<int:myid>",views.show_user_blog_details,name='viewblogs'),
    path('createblog',views.createblog,name="crating a blog")
]