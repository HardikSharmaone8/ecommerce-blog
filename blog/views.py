from django.shortcuts import render
from .models import DatabaseBlog, PublishBlog

# Create your views here.
def show_blog(request):
    #display database blogs logic
    all_blog =[]
    blog_title = DatabaseBlog.objects.values('BlogTitle')
    blog_title_setComprehension = {item['BlogTitle'] for item in blog_title}

    # display user blog logic
    user_blog = PublishBlog.objects.values('Blogger_Title')
    # print("creating blog by the user",user_blog)
    user_posted_blog = user_blog.values()
    # print("adfasfdsjklfaskdhfdshhf",user_posted_blog)
    for cat in blog_title_setComprehension:
        get_all_blog_category_data = DatabaseBlog.objects.filter(BlogTitle=cat)
        # print(get_all_blog_category_data.values())

        all_blog.append([get_all_blog_category_data.values,user_posted_blog])


    print("Value of all Blog0",all_blog)
    params = {
        "blogDetails" : all_blog
    }
    print(params)
    return render(request,'blog/index.html',params)

def show_blog_details(request,myid):
    parti_blog = DatabaseBlog.objects.filter(id=myid)
    print("jsdfkjs;kljaslfjlsdk;lsjf",parti_blog)
    params ={"particular_blog":parti_blog}


    return render(request,'blog/contentdetails.html',params)

def show_user_blog_details(request,myid):
    parti_blog = PublishBlog.objects.filter(id=myid)
    print("jsdfkjs;kljaslfjlsdk;lsjf", parti_blog)
    params ={"particular_blog":parti_blog}


    return render(request,'blog/userContentDetails.html',params)

def createblog(request):
    if request.method == "POST":
        author_name = request.POST.get('author_name','')
        email= request.POST.get('email','')
        blog_title = request.POST.get('title','')
        content = request.POST.get('content','')
        image = 'shop/image/'+request.POST.get('pic','')
        postBlog = PublishBlog(Author_Name=author_name,Blogger_Email=email,Blogger_Title=blog_title,Blogger_Content=content,Blog_Image=image)
        postBlog.save();

        check = True
        return render(request, 'blog/createblog.html',{ "check" : check })


    return render(request,'blog/createblog.html')