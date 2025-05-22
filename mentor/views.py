from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate, login, logout
from asosiy.views import Darslar, Guruh, Asosiy_talabalar_safi, Teacher_table


def LLogautview(request):
    logout(request)
    return redirect('/mentor/mentorlogin/')


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
    def get(self, request):
        if request.user.is_authenticated:
            son = Darslar.objects.filter(teacher_fk__user=request.user).count()

            guruhlar = Darslar.objects.filter(teacher_fk__user=request.user)
            l = []
            for i in guruhlar:
                l.append(i.guruh_fk)
            talaba = Asosiy_talabalar_safi.objects.all()
            num = 0
            for i in talaba:
                if i.guruh_fk in l:
                    num += 1

            guruhlarrr = list()  # mentorga tegishli bolgan guruhlarning nomi korsatilgan list
            for kk in guruhlar:
                guruhlarrr.append(kk.guruh_fk.guruh_nom)

            baholashlar = Baholash.objects.filter(teacher_fk__user=request.user)
            alo_ballar = [0] * len(guruhlarrr)
            yaxshi_ballar = [0] * len(guruhlarrr)
            past_ballar = [0] * len(guruhlarrr)
            yomon_ballar = [0] * len(guruhlarrr)
            for baholash in baholashlar:
                guruh_index = guruhlarrr.index(str(baholash.guruh_fk))
                if baholash.asosiy_talabalar_safi_fk:
                    if 90 <= (baholash.min_ball / baholash.max_ball) * 100 <= 100:
                        alo_ballar[guruh_index] += 1

                    elif 60 <= (baholash.min_ball / baholash.max_ball) * 100 < 90:
                        yaxshi_ballar[guruh_index] += 1

                    elif 30 <= (baholash.min_ball / baholash.max_ball) * 100 < 60:
                        past_ballar[guruh_index] += 1
                    elif 0 <= (baholash.min_ball / baholash.max_ball) * 100 < 30:
                        yomon_ballar[guruh_index] += 1
            alo_sum = sum(alo_ballar)
            yaxshi_sum = sum(yaxshi_ballar)
            pas_sum = sum(past_ballar)
            yomon_sum = sum(yomon_ballar)

            guruhlar_soni = []
            for k in range(len(guruhlar)):
                guruhlar_soni.append(k)

            data = {
                'gr': son,
                'son': num,

                'guruhlar': guruhlarrr,
                'alo_ballar': alo_ballar,
                'yaxshi_ballar': yaxshi_ballar,
                'pas_ballar': past_ballar,
                'yomon_ballar': yomon_ballar,
                'teacher': Teacher_table.objects.get(user=request.user),
                'alo_sum': alo_sum,
                'yaxshi_sum': yaxshi_sum,
                'pas_sum': pas_sum,
                'yomon_sum': yomon_sum,
                'guruhlar_soni': guruhlar_soni
            }

            return render(request, 'indexteacher.html', data)

        return redirect('/mentor/mentorlogin/')


class Reja(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'reja': Mavzu.objects.filter(teacher_fk__user=request.user)
            }
            return render(request, 'reja.html', data)
        return redirect('/mentor/mentorlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Mavzu.objects.create(
                nom=request.POST.get('nom'),
                link=request.POST.get('link'),
                description=request.POST.get('tarif'),
                teacher_fk=Teacher_table.objects.get(user=request.user)
            )
            return redirect('/mentor/reja/')
        return redirect('/mentor/mentorlogin/')


def RejaDelete(request, pk):
    if request.user.is_authenticated:
        if Teacher_table.objects.get(user=request.user):
            Mavzu.objects.get(id=pk).delete()
            return redirect('/mentor/reja/')
    return redirect('/mentor/mentorlogin/')


class GuruhlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'guruh': Darslar.objects.filter(teacher_fk__user=request.user),
                'talabalar': Asosiy_talabalar_safi.objects.all()
            }
            return render(request, 'guruh.html', data)
        return redirect('/mentor/mentorlogin/')


class Davomatt(View):

    def get(self, request, pk):
        if request.user.is_authenticated:
            talaba = Baholash.objects.filter(guruh_fk__guruh_nom=pk)
            talaba_uzlashtirish = dict()
            for i in talaba:
                baho = (i.min_ball / i.max_ball) * 100
                talaba_uzlashtirish[i.asosiy_talabalar_safi_fk.id] = baho
            data = {
                'talabalar': Asosiy_talabalar_safi.objects.filter(guruh_fk__guruh_nom=pk),
                'mavzu': Mavzu.objects.filter(teacher_fk__user=request.user),
                'uzlashtirish': talaba_uzlashtirish
            }
            return render(request, 'davomat.html', data)
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
    def get(self, request, pk):
        if request.user.is_authenticated:
            talaba = Baholash.objects.filter(guruh_fk__guruh_nom=pk)
            talaba_uzlashtirish = dict()
            for i in talaba:
                baho = (i.min_ball / i.max_ball) * 100
                talaba_uzlashtirish[i.asosiy_talabalar_safi_fk.id] = baho
            data = {
                'talabalar': Asosiy_talabalar_safi.objects.filter(guruh_fk__guruh_nom=pk),
                'mavzu': Mavzu.objects.filter(teacher_fk__user=request.user),
                'uzlashtirish': talaba_uzlashtirish

            }
            return render(request, 'uzlashtrish.html', data)
        return redirect('/mentor/mentorlogin/')

    def post(self, request, pk):
        if request.user.is_authenticated:
            mavzu_fkk = Mavzu.objects.get(id=request.POST.get('mavzu'))
            umumiy_ball = request.POST.get('umumiy_ball')
            talabalar = Asosiy_talabalar_safi.objects.filter(guruh_fk__guruh_nom=pk)
            for i in talabalar:
                Baholash.objects.create(
                    mavzu_fk=mavzu_fkk,
                    guruh_fk=Guruh.objects.get(guruh_nom=pk),
                    asosiy_talabalar_safi_fk=i,
                    min_ball=request.POST.get(f'min_{i.id}'),
                    max_ball=umumiy_ball,
                    teacher_fk=Teacher_table.objects.get(user=request.user)
                )
            return redirect('/mentor/guruh/')
        return redirect('/mentor/mentorlogin/')


class Konfrensiyaa(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'gr': Darslar.objects.filter(teacher_fk__user=request.user),
                'mavzu': Konfrensiya.objects.filter(teacher_fk__user=request.user)
            }
            return render(request, 'kanfrensa.html', data)
        return redirect('/mentor/mentorlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Konfrensiya.objects.create(
                batafsil=request.POST.get('batafsil'),
                link=request.POST.get('link'),
                guruh=Darslar.objects.get(id=request.POST.get('guruh')).guruh_fk,
                teacher_fk=Teacher_table.objects.get(user=request.user),
                vaqt=request.POST.get('kun'),
                soat=request.POST.get('soat'),
            )
            return redirect('/mentor/konfensiya/')
        return redirect('/mentor/mentorlogin/')


def KonfrensiyaDelete(request, pk):
    if request.user.is_authenticated:
        if Teacher_table.objects.get(user=request.user):
            Konfrensiya.objects.get(id=pk).delete()
            return redirect('/mentor/konfensiya/')
    return redirect('/mentor/mentorlogin/')


class BittaTalaba(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            bitaTalaba = Asosiy_talabalar_safi.objects.get(id=pk)
            # davomat=Davomat.objects.get(asosiy_talabalar_safi_fk__id=pk)
            alo, yaxshi, yomon, pas = [], [], [], []
            baholashTalaba = Baholash.objects.filter(asosiy_talabalar_safi_fk__id=pk)  # aliyev vali
            for i in baholashTalaba:
                if 90 <= (i.min_ball / i.max_ball) * 100 <= 100:
                    alo.append(1)

                elif 60 <= (i.min_ball / i.max_ball) * 100 < 90:
                    yaxshi.append(1)

                elif 30 <= (i.min_ball / i.max_ball) * 100 < 60:
                    pas.append(1)
                elif 0 <= (i.min_ball / i.max_ball) * 100 < 30:
                    yomon.append(1)
            data = {
                'bitatalaba': bitaTalaba,
                # 'davomat':davomat,
                'mentor': Teacher_table.objects.get(user=request.user),
                'alo': len(alo),
                'yaxshi': len(yaxshi),
                'pas': len(pas),
                'yomon': len(yomon),
                # 'qoldirilgan_darslar_soni':num
            }
            return render(request, 'talaba_profil.html', data)
        return redirect('/mentor/mentorlogin/')


class Saqlanmalar(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'eslatma': Notion.objects.filter(teacher_fk=Teacher_table.objects.get(user=request.user))
            }
            return render(request, 'nodelist.html', data)
        return redirect('/mentor/mentorlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Notion.objects.create(
                teacher_fk=Teacher_table.objects.get(user=request.user),
                eslatma=request.POST.get('eslatma')
            )
            return redirect('/mentor/saqlamalar/')
        return redirect('/mentor/mentorlogin/')


def SaqlanganlarDelete(request, pk):
    if request.user.is_authenticated:
        if Teacher_table.objects.get(user=request.user):
            Notion.objects.get(id=pk).delete()
            return redirect('/mentor/saqlamalar/')
    return redirect('/mentor/mentorlogin/')
