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

def search(request):

    blog_searched_value = request.GET.get('search','')
    all_blog = []

    # when user search blog in published blog database
    user_blog = PublishBlog.objects.values('Blogger_Title')
    user_blog_setComprehension = {item['Blogger_Title'] for item in user_blog}

    for blog in user_blog_setComprehension:
        get_all_userblog_data = PublishBlog.objects.filter(Blogger_Title=blog)
        print("GET_ALL_USERBLOG_DATA",get_all_userblog_data[0].Author_Name)
        if blog_searched_value in get_all_userblog_data[0].Author_Name.lower() or blog_searched_value in get_all_userblog_data[0].Blogger_Content.lower() or blog_searched_value in get_all_userblog_data[0].Blogger_Title.lower():
            all_blog.append(get_all_userblog_data)

    # logic when user search blof in database
    blog_title = DatabaseBlog.objects.values('BlogTitle')
    blog_title_setComprehension = {item['BlogTitle'] for item in blog_title}
    for cat in blog_title_setComprehension:
        get_all_blog_data = DatabaseBlog.objects.filter(BlogTitle=cat)
        print("Get_All_BLOG_DATA",get_all_blog_data[0].BlogAuthor)
        if blog_searched_value in get_all_blog_data[0].BlogDetails.lower() or blog_searched_value in get_all_blog_data[0].BlogTitle.lower() or blog_searched_value in get_all_blog_data[0].BlogMoral.lower() or  blog_searched_value in get_all_blog_data[0].BlogAuthor.lower():
            all_blog.append(get_all_blog_data)


    print("Value of all Blog0", all_blog)

    print(len(all_blog))
    if len(all_blog) == 0:
        check = True
        return render(request, 'blog/search.html', {"check":check})
    else:
        params = {
            "blogDetails": all_blog
        }
        print(params)
        return render(request, 'blog/search.html', params)




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