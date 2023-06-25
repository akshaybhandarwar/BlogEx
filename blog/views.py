from django.shortcuts import render, HttpResponse
from blog.models import Blog,Contact

# Create your views here.

def home(request):
    # return HttpResponse("sjdsjclsjnclj")
    return render(request,'index.html')


def blog(request):
   no_of_posts=5
   page=request.GET.get('page')
   if page is None:
       page=1
   else:
      page=int(page)   
   # print(request.GET.get('pageno'))
   print(page)  
   blogs=Blog.objects.all()[(page-1)*no_of_posts:page*no_of_posts]
   context={'blogs':blogs}
   return render(request,'bloghome.html',context)

def blogpost(request, slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render( request,'blogpost.html',context)

def search(request):

   return render(request,'search.html')

def contact(request):
   if request.method=='POST':
      name=request.POST.get("name")
      email=request.POST.get("email")
      phone=request.POST.get("phone")
      desc=request.POST.get("desc")
      inst=Contact(name=name,email=email,phone=phone,desc=desc)
      inst.save()
     
   return render(request,'contact.html')