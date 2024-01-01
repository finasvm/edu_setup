from django.shortcuts import render,redirect
from django.views.generic import View,CreateView
from django.contrib.auth import authenticate,login
from .models import *

# Create your views here.

# class Login(View):
#     def get(self,request):
#         return render(request,'login.html')
#     def post(self,request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(password)
#         user=authenticate(request,username=username,password=password)
#         if user:
#            print(user)
#            login(request,user)
#            print(user.username)
#            return redirect('userhome')
       
#         else:
#            return redirect('login')
        
class Home(View):
    def get(self,request):
        course=education.objects.all()
        return render(request,'userhome.html',{'course':course})
    

class addprod(CreateView):
   def get(self,request):
       return render(request,'addstuf.html')                   
   def post(self,request):
       if request.method == 'POST':
            name = request.POST['username']
            email = request.POST['email']
            course = request.POST['course']
            university = request.POST['university']
            year = request.POST['year']
            userpart = Userside.objects.create(name=name,email=email)
            Eductaiondetails.objects.create(course=course,university=university,year=year,
            userdet=userpart) 
            return redirect('userhome')
       
class DelProd(View):
    def get(self,request,id):
        prod = education.objects.get(id=id)
        prod.delete()
        return redirect('userhome')