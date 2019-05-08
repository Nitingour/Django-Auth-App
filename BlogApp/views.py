from django.shortcuts import render
from BlogApp.forms import SignupForm,BlogForm
from django.contrib.auth.decorators import login_required
from BlogApp.models import Blog
# Create your views here.
def index(request):
    return render(request,'BlogApp/index.html')

@login_required
def newblog(request):
    if request.method=="POST":
        print('POST Calling')
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.author=request.user
            data.save()
            print('Data save successfully')
            form=BlogForm()
            mydict={'form':form,'msg':'Blog Posted Succssfully...'}
            return render(request,"BlogApp/newblog.html",context=mydict)
    else:
        form=BlogForm()
        return render(request,'BlogApp/newblog.html',{'form':form})

def viewblogs(request):
    blogs=Blog.objects.all().order_by('-upload_date')
    return render(request,'BlogApp/viewblog.html',{'blogs':blogs})

def signupview(request):
    if request.method=='GET':
        sform=SignupForm()
        return render(request,"BlogApp/signup.html",{'sform':sform})
    if request.method=='POST':
        sform=SignupForm(request.POST)
        user=sform.save()
        user.set_password(user.password)
        user.save()
        sform=SignupForm()
        mydict={'sform':sform,'msg':'Registration Succssfully...'}
        return render(request,"BlogApp/signup.html",context=mydict)
