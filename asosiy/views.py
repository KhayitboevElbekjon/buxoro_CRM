from django.shortcuts import render,redirect
from django.views import View
from .models import *
# from mentor.models import *
from django.contrib.auth import authenticate,login,logout

from mentor.models import Davomat
from django.http import HttpResponseRedirect

def logautview(request):
    logout(request)
    return redirect('/adminlogin/')
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
    def get(self,request,son):
        # kk=Kurs.objects.get(id=son)
        if request.user.is_authenticated:
            Kurs.objects.get(id=son).delete()
            return redirect('/asosiy/kurslar/')
        return redirect('/adminlogin/')
class Guruhlar(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'kurs':Kurs.objects.all(),
                'guruhlar':Guruh.objects.all()
            }
            return render(request,'guruhadmin.html',data)
        return redirect('/adminlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Guruh.objects.create(
                kurs_fk=Kurs.objects.get(id=request.POST.get('kurs')),
                guruh_nom=request.POST.get('nom'),
                ochilgan_sana=request.POST.get('sana'),
                davomiyligi=request.POST.get('davomiyligi')
            )
            return redirect('/asosiy/guruhlar/')
        return redirect('/adminlogin/')

class GuruhDelete(View):
    def get(self,request,son):
        if request.user.is_authenticated:
            Guruh.objects.get(id=son).delete()
            return redirect('/asosiy/guruhlar/')
        return redirect('/adminlogin/')
class Sorovlar(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'sorovlar':Sorov.objects.all(),
                'kurs':Kurs.objects.all()
            }
            return render(request,'talabgorTalabalar.html',data)
        return redirect('/adminlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Sorov.objects.create(
                ism=request.POST.get('ism'),
                fam=request.POST.get('fam'),
                tel=request.POST.get('tel'),
                kurs_fk=Kurs.objects.get(id=request.POST.get('kurs'))
            )
            return redirect('/asosiy/sorov/')
        return redirect('/adminlogin/')
class Kutayotganlar(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'kutush':Sorov.objects.all(),
                'kutayotganlar':Kutish.objects.all()
            }
            return render(request,'kutish.html',data)
        return redirect('/adminlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Kutish.objects.create(
                sorov_fk=Sorov.objects.get(id=request.POST.get('sorov')),
                batafsil=request.POST.get('batafsil')
            )
            # Sorov.objects.get(id=request.POST.get('sorov')).delete()
            return redirect('/asosiy/kutayotganlar/')
        return redirect('/adminlogin/')

class Sinovv(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'sinovdagilar':Sinov.objects.all(),
                'kutish':Kutish.objects.all(),
                'kurs':Kurs.objects.all(),
                'guruh':Guruh.objects.all()
            }
            return render(request,'sinov.html',data)
        return redirect('/adminlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Sinov.objects.create(
                kutish_fk=Kutish.objects.get(id=request.POST.get('kutish')),
                kurs_fk=Kurs.objects.get(id=request.POST.get('kurs')),
                guruh_fk=Guruh.objects.get(id=request.POST.get('guruh')),
                vaqt=request.POST.get('vaqt')
            )
            return redirect('/asosiy/sinov')
        return redirect('/adminlogin/')

class Talabalar(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'talaba':Asosiy_talabalar_safi.objects.all(),
                'kurs':Kurs.objects.all(),
                'guruh':Guruh.objects.all(),
            }
            return render(request,'asosiy_Talabalar.html',data)
        return redirect('/adminlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Asosiy_talabalar_safi.objects.create(
                ism=request.POST.get('ism'),
                fam=request.POST.get('fam'),
                tel_1=request.POST.get('tel1'),
                tel_2=request.POST.get('tel2'),
                rasm=request.POST.get('rasm'),
                tugulgan_joy=request.POST.get('joy'),
                tugulgan_sana=request.POST.get('sana'),
                kurs_fk=Kurs.objects.get(id=request.POST.get('kurs')),
                guruh_fk=Guruh.objects.get(id=request.POST.get('guruh'))
            )
            return redirect('/asosiy/talabalar/')
        return redirect('/adminlogin/')
class DavomatAdmin(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'davomat': Davomat.objects.filter(darsga_qatnashmadi=True)
            }
            return render(request, 'davomatadmin.html',data)
        return redirect('/adminlogin/')
class Hujat(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={'hujat':Hujatlar.objects.all()}
            return render(request, 'hujjatlar.html',data)
        return redirect('/adminlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Hujatlar.objects.create(
                file=request.POST.get('file'),
                nom=request.POST.get('nom')
            )
            return redirect('/asosiy/hujat/')
        return redirect('/adminlogin/')
class Teacher(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'mentor':Teacher_table.objects.all()
            }
            return render(request, 'teacher_table.html',data)
        return redirect('/adminlogin/')

    def post(self, request):
        ismm = request.POST.get('ism')
        famm = request.POST.get('fam')
        tell = request.POST.get('raqam')
        manzill = request.POST.get('manzil')
        tugulgan_sanaa = request.POST.get('sana')
        loginn = request.POST.get('login')
        parol1 = request.POST.get('parol1')
        parol2 = request.POST.get('parol2')
        if parol1 == parol2:
            user1 = User.objects.create_user(username=loginn, password=parol2)
            Teacher_table.objects.create(
                ism=ismm,
                fam=famm,
                tel=tell,
                manzil=manzill,
                tugulgan_sana=tugulgan_sanaa,
                user=user1
            )
            return redirect('/asosiy/teacher/')

class Dars(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'kurs': Kurs.objects.all(),
                'guruh': Guruh.objects.all(),
                'mentor':Teacher_table.objects.all(),
                'darslar':Darslar.objects.all()
            }
            return render(request, 'darslaradmin.html',data)
        return redirect('/adminlogin/')
    def post(self,request):

        if request.user.is_authenticated:
            Darslar.objects.create(
                kurs_fk=Kurs.objects.get(id=request.POST.get('kurs')),
                guruh_fk=Guruh.objects.get(id=request.POST.get('guruh')),
                teacher_fk=Teacher_table.objects.get(id=request.POST.get('mentor')),
                hafta_kunlari=request.POST.get('toq'),
                dars_boshlanish_vaqti=request.POST.get('vaqt')
            )
            return redirect('/asosiy/dars/')
        return redirect('/adminlogin/')

def SorovDelete(request,pk):
    if request.user.is_authenticated:
        Sorov.objects.get(id=pk).delete()
        return redirect('/asosiy/sorov/')
    return redirect('/adminlogin/')

def KutushDelete(request,pk):
    if request.user.is_authenticated:
        Kutish.objects.get(id=pk).delete()
        return redirect('/asosiy/kutayotganlar/')
    return redirect('/adminlogin/')

def SinovDelete(request,pk):
    if request.user.is_authenticated:
        Sinov.objects.get(id=pk).delete()
        return redirect('/asosiy/sinov/')
    return redirect('/adminlogin/')

def TalabaDelete(request,pk):
    if request.user.is_authenticated:
        Asosiy_talabalar_safi.objects.get(id=pk).delete()
        return redirect('/asosiy/talabalar/')
    return redirect('/adminlogin/')

def TeacherDelete(request,pk):
    if request.user.is_authenticated:
        Teacher_table.objects.get(id=pk).delete()
        return redirect('/asosiy/teacher/')
    return redirect('/adminlogin/')