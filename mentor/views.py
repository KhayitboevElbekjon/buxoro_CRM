from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate,login,logout
from asosiy.views import Darslar,Guruh,Asosiy_talabalar_safi,Teacher_table



class Mentorlogin(View):
    def post(self, request):
        loginn = request.POST.get('login')
        parol = request.POST.get('parol')
        user = authenticate(request, username=loginn, password=parol)
        if user is None:
            return redirect('/mentor/mentorlogin')
        login(request, user)
        return redirect('/mentor/indexteacher')

    def get(self, request):
        return render(request, 'loginteacher.html')
class IndexTeacher(View):
    def get(self,request):
        if request.user.is_authenticated:
            son=Darslar.objects.filter(teacher_fk__user=request.user).count()

            guruhlar=Darslar.objects.filter(teacher_fk__user=request.user)
            l=[]
            for i in guruhlar:
                l.append(i.guruh_fk)
            talaba=Asosiy_talabalar_safi.objects.all()
            num=0
            for i in talaba:
                if i.guruh_fk in l:
                    num+=1
            data={
                'gr':son,
                'son':num
            }
            return render(request,'indexteacher.html',data)

        return redirect('/mentor/mentorlogin/')
class Reja(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'reja':Mavzu.objects.filter(teacher_fk__user=request.user)
            }
            return render(request, 'reja.html',data)
        return redirect('/mentor/mentorlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Mavzu.objects.create(
                nom=request.POST.get('nom'),
                link=request.POST.get('link'),
                description=request.POST.get('tarif'),
                teacher_fk=Teacher_table.objects.get(user=request.user)
            )
            return redirect('/mentor/reja/')
        return redirect('/mentor/mentorlogin/')
def RejaDelete(request,pk):
    if request.user.is_authenticated:
        if Teacher_table.objects.get(user=request.user):
            Mavzu.objects.get(id=pk).delete()
            return redirect('/mentor/reja/')
    return redirect('/mentor/mentorlogin/')

class GuruhlarView(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'guruh':Darslar.objects.filter(teacher_fk__user=request.user),
                'talabalar':Asosiy_talabalar_safi.objects.all()
            }
            return render(request, 'guruh.html',data)
        return redirect('/mentor/mentorlogin/')

class Davomatt(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            data={
                'talabalar':Asosiy_talabalar_safi.objects.filter(guruh_fk__guruh_nom=pk),
                'mavzu':Mavzu.objects.filter(teacher_fk__user=request.user) }
            return render(request, 'davomat.html',data)
        return redirect('/mentor/mentorlogin/')
    def post(self, request, pk):
        if request.user.is_authenticated:
            talabalar = request.POST.getlist('davomat')
            mavzu_fkk = Mavzu.objects.get(id=request.POST.get('mavzu'))
            guruh_fk = Guruh.objects.get(guruh_nom=pk)
            for talaba_id in talabalar:
                talaba = Asosiy_talabalar_safi.objects.get(id=talaba_id)
                Davomat.objects.create(
                    mavzu_fk=mavzu_fkk,
                    guruh_fk=guruh_fk,
                    asosiy_talabalar_safi_fk=talaba,
                    darsga_qatnashmadi=True,
                    teacher_fk=Teacher_table.objects.get(user=request.user),
                )
            return redirect('/mentor/guruh/')
        return redirect('/mentor/mentorlogin/')



class Ozlashtirish(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            data={
                'talabalar':Asosiy_talabalar_safi.objects.filter(guruh_fk__guruh_nom=pk),
                'mavzu':Mavzu.objects.filter(teacher_fk__user=request.user)

            }
            return render(request, 'uzlashtrish.html',data)
        return redirect('/mentor/mentorlogin/')
    def post(self,request,pk):
        if request.user.is_authenticated:
            mavzu_fkk=Mavzu.objects.get(id=request.POST.get('mavzu'))
            umumiy_ball=request.POST.get('umumiy_ball')
            talabalar = Asosiy_talabalar_safi.objects.filter(guruh_fk__guruh_nom=pk)
            for i in talabalar:
                Baholash.objects.create(
                    mavzu_fk=mavzu_fkk,
                    guruh_fk=Guruh.objects.get(guruh_nom=pk),
                    asosiy_talabalar_safi_fk=i,
                    min_ball=request.POST.get(f'min_{i.id}'),
                    max_ball=umumiy_ball
                )
            return redirect('/mentor/guruh/')
        return redirect('/mentor/mentorlogin/')
class Konfrensiyaa(View):
    def get(self,request):
        if request.user.is_authenticated:
            data={
                'gr':Darslar.objects.filter(teacher_fk__user=request.user),
                'mavzu':Konfrensiya.objects.filter(teacher_fk__user=request.user)
            }
            return render(request, 'kanfrensa.html',data)
        return redirect('/mentor/mentorlogin/')
    def post(self,request):
        if request.user.is_authenticated:
            Konfrensiya.objects.create(
            batafsil=request.POST.get('batafsil'),
            link = request.POST.get('link'),
            guruh = Darslar.objects.get(id=request.POST.get('guruh')).guruh_fk,
            teacher_fk=Teacher_table.objects.get(user=request.user),
                vaqt=request.POST.get('kun'),
                soat=request.POST.get('soat'),
            )
            return redirect('/mentor/konfensiya/')
        return redirect('/mentor/mentorlogin/')
def KonfrensiyaDelete(request,pk):
    if request.user.is_authenticated:
            if Teacher_table.objects.get(user=request.user):
                Konfrensiya.objects.get(id=pk).delete()
                return redirect('/mentor/konfensiya/')
    return redirect('/mentor/mentorlogin/')
class BittaTalaba(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            # soni=Davomat.objects.filter(darsga_qatnashmadi=False)
            # num=0
            # for i in soni:
            #     if i.asosiy_talabalar_safi_fk==Asosiy_talabalar_safi.objects.get(id=pk):
            #         num+=1
            data={
                'bitatalaba':Asosiy_talabalar_safi.objects.get(id=pk),
                'mentor':Teacher_table.objects.get(user=request.user),
                # 'qoldirilgan_darslar_soni':num
            }
            return render(request,'talaba_profil.html',data)
        return redirect('/mentor/mentorlogin/')
class Saqlanmalar(View):
    def get(self,request):
        if request.user.is_authenticated:

            return render(request,'nodelist.html')
        return redirect('/mentor/mentorlogin/')