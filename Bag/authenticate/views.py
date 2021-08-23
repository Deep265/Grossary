from django.shortcuts import render,reverse,redirect,get_object_or_404

# Models Import
from .models import SignUp
from django.contrib.auth.models import User

# Http Imports
from django.http import HttpResponse,HttpResponseRedirect

# Login imports
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Message Imports
from django.contrib import messages



# Create your views here.

# Sign,Login
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        age = request.POST.get("age")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        image = request.FILES.get("image")

        user = User(first_name=first_name,last_name=last_name,username=username,email=email)
        user.set_password(password)
        user.save()
        user_extra = SignUp(phone=phone,address=address,age=age,user=user,image=image)
        user_extra.save()
        return HttpResponseRedirect('/authenticate/login/')
    return render(request,'authenticate/signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('bag:Home'))
            else:
                return HttpResponseRedirect("User is Not Active")
        else:
            messages.error(request,"User or Password is Invalid")
            return HttpResponseRedirect(reverse('authenticate:login'))
    return render(request,'authenticate/login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/authenticate/login/')



# Profile Section
@login_required(login_url='/authenticate/login/')
def my_profile(request,pk):
    user = get_object_or_404(User,pk=pk)
    more_info = get_object_or_404(SignUp,pk=user.prof.pk)
    return render(request,"authenticate/profile.html",context={"user_info":user,"more_info":more_info})

def change_photo(request,pk):
    user = get_object_or_404(User,pk=pk)
    more_info = get_object_or_404(SignUp,pk=user.prof.pk)
    if request.method == "POST":
        image = request.FILES.get("image")
        more_info.image = image
        more_info.save()
        return HttpResponseRedirect(reverse('bag:Home'))
    return render(request,"authenticate/change_profile_photo.html")

@login_required(login_url='/authenticate/login/')
def change_profile(request,pk):
    user = get_object_or_404(User,pk=pk)
    more_info = get_object_or_404(SignUp,pk=user.prof.pk)
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address =request.POST.get("address")


        # update
        user.username = username
        user.email = email
        more_info.phone = phone
        more_info.address = address

        user.save()
        more_info.save()
        return HttpResponseRedirect('/authenticate/profile/'+str(pk))
    return render(request,"authenticate/edit_profile.html",context={"user_info":user,"more_info":more_info})

@login_required(login_url='/authenticate/login/')
def ChangePassword(request,pk):
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request,'Password does not matched')
            return redirect('/authenticate/login/')
        else:
            user.set_password(password)
            user.save()
    return render(request,'authenticate/change_password.html')




