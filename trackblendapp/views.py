from django.shortcuts import render,redirect
from trackblendapp.forms import userForm,userprofileForm
from trackblendapp.models import userdetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"accounts/home.html",{})

def register(request):
    registered = False
    if request.method == 'POST':
        form1 = userForm(request.POST)
        form2 = userprofileForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            
            profile = form2.save(commit=False)
            profile.user = user 
            profile.save()
            registered = True
            return redirect('trackblendapp:login')
    else:
        form1 = userForm()
        form2 = userprofileForm()
    context = {
        'form1':form1,
        'form2':form2,
        'registered':registered
    }
    return render(request,"accounts/registeration.html",context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return redirect('trackblendapp:home')
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("Please check your creds")
    return render(request,"accounts/login.html")

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('trackblendapp:login')


@login_required(login_url='login')
def dashboard(request):
    data = userdetails.objects.get(user=request.user)
    print(data)
    context = {
        'data':data
    }
    return render(request,"accounts/dashboard.html",context)
