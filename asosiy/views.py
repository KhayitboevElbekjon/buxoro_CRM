from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate,login,logout

class AdminLogin(View):
    def post(self, request):
        loginn = request.POST.get('login')
        parol = request.POST.get('parol')
        user = authenticate(request, username=loginn, password=parol)
        if user is None:
            return redirect('/adminlogin/')
        login(request, user)
        return redirect('/asosiy/IndexAdmin')

    def get(self, request):
        return render(request, 'loginadmin.html')

class IndexAdmin(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'ustoz': Teacher_table.objects.all().count(),
                'sinovdagi_talabalar':Sinov.objects.all().count(),
                'asosiy_talabalar':Asosiy_talabalar_safi.objects.all().count(),
                'talabgor_talabalar':Kutish.objects.all().count(),
                'sorov':Sorov.objects.all()
            }
            return render(request,'indexadmin.html',data)
        return redirect('/adminlogin/')
# --------------------------------------------------------------------------------------------

class Kurslar(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'kurslar':Kurs.objects.all()
            }
            return render(request, 'kurs.html',data)
        return redirect('/adminlogin/')
    def post(self, request):
        if request.user.is_authenticated:
            Kurs.objects.create(
                nom=request.POST.get('nom'),
                ochilgan_sana=request.POST.get('vaqt')
            )
            return redirect('/asosiy/kurslar')  # Kurs qoshish uchun
        return redirect('/adminlogin/')
class  KursDelete(View):
    def post(self,request,son):
        if request.user.is_authenticated:
            Kurs.objects.filter(id=son).delete()
            return redirect('/asosiy/kurslar')
        return redirect('/adminlogin/')
class Guruhlar(View):
    def get(self,request):
        return render(request,'guruhadmin.html')