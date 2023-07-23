from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate,login,logout

class Mentorlogin(View):
    def post(self, request):
        loginn = request.POST.get('login')
        parol = request.POST.get('parol')
        user = authenticate(request, username=loginn, password=parol)
        if user is None:
            return redirect('/mentor/mentorlogin')
        login(request, user)
        return redirect('/mentor/mentorlogin')

    def get(self, request):
        return render(request, 'loginteacher.html')
class IndexTeacher(View):
    def get(self,request):
        return render(request,'indexteacher.html')