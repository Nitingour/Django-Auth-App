from django.shortcuts import render
from BlogApp.forms import SignupForm
# Create your views here.
def index(request):
    return render(request,'BlogApp/index.html')

def newblog(request):
    return render(request,'BlogApp/newblog.html')

def viewblogs(request):
    return render(request,'BlogApp/viewblog.html')

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
