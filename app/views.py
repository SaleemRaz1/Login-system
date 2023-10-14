from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from .models import Registration
# Create your views here.

def SignUp(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        sex=request.POST['sex']
        email=request.POST['email']
        pwd=request.POST['password']
        my_user=Registration(firstName=fname,lastName=lname,sex=sex,email=email,password=pwd)
        my_user.save()
        return redirect('login')
    return render(request,'signup_page.html')


def Login(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['password']
        user=authenticate(request,username=email,password=pwd)
        if email==email:
            login(request,user)
            return redirect('welcom')
        else:
            return HttpResponse("Username or password is incorrect")
            
    return render(request,'login_page.html')



def Welcome(request):
    return render (request,'welcome.html') 
     
        
        
