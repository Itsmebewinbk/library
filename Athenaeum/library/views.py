from django.shortcuts import render

from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from library import forms
from django.contrib.auth import authenticate,login,logout

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:

            return render(request,"registration.html",{"form":form})


class LogInView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print("Login Succesfull")
                return redirect("index")
            else:
                print("Invalid Credentials")
                return render(request, "login.html",{"form":form})
        return render(request,"login.html")
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html",)
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
