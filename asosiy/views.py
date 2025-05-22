import math
from django.db.models import F
from django.db.models import Sum, Avg, Max, Min, Count
from django.shortcuts import render, redirect
from django.views import View
from .models import *
# from mentor.models import *
from django.contrib.auth import authenticate, login, logout

from mentor.models import Davomat
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404


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
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'ustoz': Teacher_table.objects.all().count(),
                'sinovdagi_talabalar': Sinov.objects.all().count(),
                'asosiy_talabalar': Asosiy_talabalar_safi.objects.all().count(),
                'talabgor_talabalar': Kutish.objects.all().count(),
                'sorov': Sorov.objects.all(),
                'qarizdorlar': Umumiy_shot.objects.filter(umumiy_summa__startswith='-')
            }
            return render(request, 'indexadmin.html', data)
        return redirect('/adminlogin/')


# --------------------------------------------------------------------------------------------

class Kurslar(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'kurslar': Kurs.objects.all()
            }
            return render(request, 'kurs.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Kurs.objects.create(
                nom=request.POST.get('nom'),
                ochilgan_sana=request.POST.get('vaqt')
            )
            return redirect('/asosiy/kurslar')  # Kurs qoshish uchun
        return redirect('/adminlogin/')


class KursDelete(View):
    def get(self, request, son):
        # kk=Kurs.objects.get(id=son)
        if request.user.is_authenticated:
            Kurs.objects.get(id=son).delete()
            return redirect('/asosiy/kurslar/')
        return redirect('/adminlogin/')


class Guruhlar(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'kurs': Kurs.objects.all(),
                'guruhlar': Guruh.objects.all()
            }
            return render(request, 'guruhadmin.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
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
    def get(self, request, son):
        if request.user.is_authenticated:
            Guruh.objects.get(id=son).delete()
            return redirect('/asosiy/guruhlar/')
        return redirect('/adminlogin/')


class Sorovlar(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'sorovlar': Sorov.objects.all(),
                'kurs': Kurs.objects.all()
            }
            return render(request, 'talabgorTalabalar.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
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
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'kutush': Sorov.objects.all(),
                'kutayotganlar': Kutish.objects.all()
            }
            return render(request, 'kutish.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Kutish.objects.create(
                sorov_fk=Sorov.objects.get(id=request.POST.get('sorov')),
                batafsil=request.POST.get('batafsil')
            )
            # Sorov.objects.get(id=request.POST.get('sorov')).delete()
            return redirect('/asosiy/kutayotganlar/')
        return redirect('/adminlogin/')


class Sinovv(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'sinovdagilar': Sinov.objects.all(),
                'kutish': Kutish.objects.all(),
                'kurs': Kurs.objects.all(),
                'guruh': Guruh.objects.all()
            }
            return render(request, 'sinov.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
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
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'talaba': Asosiy_talabalar_safi.objects.all(),
                'kurs': Kurs.objects.all(),
                'guruh': Guruh.objects.all()
            }
            return render(request, 'asosiy_Talabalar.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
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
            return render(request, 'davomatadmin.html', data)
        return redirect('/adminlogin/')


class Hujat(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {'hujat': Hujatlar.objects.all()}
            return render(request, 'hujjatlar.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Hujatlar.objects.create(
                file=request.FILES.get('fayl'),
                nom=request.POST.get('nom'),
                tarif=request.POST.get('tarif')

            )
            return redirect('/asosiy/hujat/')
        return redirect('/adminlogin/')


class Teacher(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'mentor': Teacher_table.objects.all()
            }
            return render(request, 'teacher_table.html', data)
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
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'kurs': Kurs.objects.all(),
                'guruh': Guruh.objects.all(),
                'mentor': Teacher_table.objects.all(),
                'darslar': Darslar.objects.all()
            }
            return render(request, 'darslaradmin.html', data)
        return redirect('/adminlogin/')

    def post(self, request):

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


def HujatOchish(request, pk):
    hujat = Hujatlar.objects.get(id=pk)
    response = FileResponse(hujat.file)
    return response


def HujatDelete(request, pk):
    if request.user.is_authenticated:
        Hujatlar.objects.get(id=pk).delete()
        return redirect('/asosiy/hujat/')
    return redirect('/adminlogin/')


def SorovDelete(request, pk):
    if request.user.is_authenticated:
        Sorov.objects.get(id=pk).delete()
        return redirect('/asosiy/sorov/')
    return redirect('/adminlogin/')


def KutushDelete(request, pk):
    if request.user.is_authenticated:
        Kutish.objects.get(id=pk).delete()
        return redirect('/asosiy/kutayotganlar/')
    return redirect('/adminlogin/')


def SinovDelete(request, pk):
    if request.user.is_authenticated:
        Sinov.objects.get(id=pk).delete()
        return redirect('/asosiy/sinov/')
    return redirect('/adminlogin/')


def TalabaDelete(request, pk):
    if request.user.is_authenticated:
        Asosiy_talabalar_safi.objects.get(id=pk).delete()
        return redirect('/asosiy/talabalar/')
    return redirect('/adminlogin/')


def TeacherDelete(request, pk):
    if request.user.is_authenticated:
        Teacher_table.objects.get(id=pk).delete()
        return redirect('/asosiy/teacher/')
    return redirect('/adminlogin/')


class Moliya(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'moliya.html')
        return redirect('/adminlogin/')


class Shot(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            talaba = Asosiy_talabalar_safi.objects.get(id=pk)
            shot_tarixi = Tolov.objects.filter(asosiy_talabalar_safi_fk__id=pk)
            umumiy_summaa = Umumiy_shot.objects.filter(asosiy_talabalar_safi_fk=talaba).last()
            data = {
                'talaba': talaba,
                'shot_tarixi': shot_tarixi,
                'Umumiy_summa': umumiy_summaa
            }
            return render(request, 'shot_kiritish.html', data)
        return redirect('/adminlogin/')

    def post(self, request, pk):
        if request.user.is_authenticated:
            asosiy_talaba = Asosiy_talabalar_safi.objects.get(id=pk)
            summa = request.POST.get('summa')
            tolov_qilgan_shaxs = request.POST.get('shaxs')

            try:
                umumiy_shott = Umumiy_shot.objects.filter(asosiy_talabalar_safi_fk=asosiy_talaba).last()
                if umumiy_shott is None:
                    umumiy_shott = Umumiy_shot.objects.create(asosiy_talabalar_safi_fk=asosiy_talaba, umumiy_summa=0)
            except Umumiy_shot.DoesNotExist:
                umumiy_shott = Umumiy_shot.objects.create(asosiy_talabalar_safi_fk=asosiy_talaba, umumiy_summa=0)

            summaaa = int(summa)
            umumiy_shott.umumiy_summa += summaaa
            umumiy_shott.save()

            Tolov.objects.create(
                asosiy_talabalar_safi_fk=asosiy_talaba,
                summa=summa,
                tolov_qilgan_shaxs=tolov_qilgan_shaxs,
                tolov_qilgan_shaxs_tel=request.POST.get('tel')
            )

            Umumiy_shot.objects.create(
                asosiy_talabalar_safi_fk=asosiy_talaba,
                umumiy_summa=umumiy_shott.umumiy_summa
            )

            return render(request, 'mofaqiyat.html')
        return redirect('/adminlogin/')


class Yechib_olishsh(View):
    def get(self, request):
        if request.user.is_authenticated:
            kurs_nomi = Kurs.objects.all()

            data = {
                'kurs_nomi': kurs_nomi
            }
            return render(request, 'moliya_kirim_yechibOlish.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            kurs_id = request.POST.get('kurs_nomi')
            oy_nomi = request.POST.get('oy_nomi')

            try:
                kurs = Kurs.objects.get(id=kurs_id)
            except Kurs.DoesNotExist:
                return redirect('/asosiy/moliya')

            talabalar = Asosiy_talabalar_safi.objects.filter(kurs_fk=kurs)

            for talaba in talabalar:
                try:
                    kurs_summasi = Kurs_summa.objects.filter(kurs_fk=kurs).last()
                    shotdan_talabani_olish = Umumiy_shot.objects.filter(asosiy_talabalar_safi_fk=talaba).last()

                    if shotdan_talabani_olish:
                        shotdan_talabani_olish.umumiy_summa -= kurs_summasi.summa
                        shotdan_talabani_olish.save()

                    Yechib_olish.objects.create(
                        oy_nomi=oy_nomi,
                        kurs_fk=kurs,
                        asosiy_talabalar_safi_fk=talaba
                    )
                except (Kurs_summa.DoesNotExist, Umumiy_shot.DoesNotExist):
                    pass
            return render(request, 'kurs_tolov_muvaffaqiyatli.html')
        return redirect('/adminlogin/')


class KursSummasi(View):
    def get(self, request):
        if request.user.is_authenticated:
            kurs_nomi = Kurs.objects.all()
            data = {
                'kurs_nomi': kurs_nomi
            }
            return render(request, 'moliya_kirim_kursSummasi.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Kurs_summa.objects.create(
                kurs_fk=Kurs.objects.get(nom=request.POST.get('kurs_nomi')),
                summa=request.POST.get('summa')
            )
            return redirect('/asosiy/moliya/')
        return redirect('/adminlogin/')


class Qarizdorlar_jadvali(View):
    def get(self, request):
        if request.user.is_authenticated:
            qarizdor_talabalar = Umumiy_shot.objects.filter(umumiy_summa__startswith='-')
            data = {
                'qarizdor_talabalar': qarizdor_talabalar
            }
            return render(request, 'moliya_kirim_qarizdorlar.html', data)
        return redirect('/adminlogin/')


class MoliyaKirim(View):
    def get(self, request):
        if request.user.is_authenticated:
            moliya_kirim = Tolov.objects.all()
            data = {
                'moliya_kirim': moliya_kirim
            }
            return render(request, 'moliya_kirim_shotJadvali.html', data)
        return redirect('/adminlogin/')


class Harajatlar_kiritish(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'moliya_chiqim_kiritish.html')
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Harajat.objects.create(
                harajat_turi=request.POST.get('harajat'),
                summa=request.POST.get('summa'),
                tarif=request.POST.get('tarif')
            )
            return render(request, 'harjat_muvofaqiyatli.html')
        return redirect('/adminlogin/')


class Barcha_Harajatlar(View):
    def get(self, request):
        if request.user.is_authenticated:
            barcha_harajatlar = Harajat.objects.all()
            data = {
                'barcha_harajatlar': barcha_harajatlar
            }
            return render(request, 'molya_chiqim_Jadvali.html', data)
        return redirect('/adminlogin/')


class MoliyaDiagramma(View):
    def get(self, request):
        if request.user.is_authenticated:
            harajat = Harajat.objects.all()

            Oylik = list()
            Soliq = list()
            Reklama = list()
            Kamunal = list()
            ragbatlantirish = list()
            Boshqalar = list()
            for i in harajat:
                if i.harajat_turi == 'Oylik':
                    Oylik.append(1)
                elif i.harajat_turi == 'Soliq':
                    Soliq.append(1)
                elif i.harajat_turi == 'Reklama':
                    Reklama.append(1)
                elif i.harajat_turi == 'Kamunal xizmatlar':
                    Kamunal.append(1)
                elif i.harajat_turi == "Rag'batlantirish":
                    ragbatlantirish.append(1)
                elif i.harajat_turi == 'Boshqalar':
                    Boshqalar.append(1)
            oylik_sum = len(Oylik)
            soliq_sum = len(Soliq)
            reklama_sum = len(Reklama)
            komunal_sum = len(Kamunal)
            ragbatlantirish_sum = len(ragbatlantirish)
            boshqalar_sum = len(Boshqalar)
            data = {
                'oylik_sum': oylik_sum,
                'soliq_sum': soliq_sum,
                'reklama_sum': reklama_sum,
                'komunal_sum': komunal_sum,
                'ragbatlantirish_sum': ragbatlantirish_sum,
                'boshqalar_sum': boshqalar_sum
            }

            return render(request, 'moliya_diagramm.html', data)
        return redirect('/adminlogin/')


class Oqituvchi_oyligi(View):
    def get(self, request):
        if request.user.is_authenticated:
            taqsimot = Teacher_table.objects.all()
            data = {
                'taqsimot': taqsimot
            }
            return render(request, 'moliya_chiqimTeacher.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            mentor_id = request.POST.get('oylik')
            oy = request.POST.get('oy')
            summaa = request.POST.get('summa')

            Mentor_oylik.objects.create(
                mentor_fk=Teacher_table.objects.get(id=mentor_id),
                oy_nomi=oy,
                summa=summaa
            )
            Harajat.objects.create(
                harajat_turi='Oylik',
                summa=summaa,
                tarif=f"{Teacher_table.objects.get(id=mentor_id)}ga,{oy} oyi uchun {summaa} so'm miqdorda pul o'tkazildi!"

            )
            return render(request, 'mentor_muvofaqiyatli.html')

        return redirect('/adminlogin/')


class Oylik_jadval(View):
    def get(self, request):
        if request.user.is_authenticated:
            oylik_chiqim = Mentor_oylik.objects.all()
            data = {
                'oylik': oylik_chiqim
            }
            return render(request, 'moliya_chiqimTeacherTable.html', data)
        return redirect('/adminlogin/')


import requests


class Qarizdorlar_SMS(View):
    def get(self, request):
        if request.user.is_authenticated:
            qarizdorlar = Umumiy_shot.objects.filter(umumiy_summa__startswith='-')
            url = "https://notify.eskiz.uz/api/message/sms/send"
            for i in qarizdorlar:
                tel_nomer = i.asosiy_talabalar_safi_fk.tel_2[1::]
                xabar = f"Assalomu alaykum.{i.asosiy_talabalar_safi_fk.ism} {i.asosiy_talabalar_safi_fk.fam}ning NodirbekEdu o'quv markazdagi qarizdoriligi {0 - i.umumiy_summa} so'mga yetdi! Iltimos qarizdorlikni bartaraf qiling!!!"
                payload = {'mobile_phone': tel_nomer,
                           'message': xabar,
                           'from': '4546',
                           'callback_url': 'http://0000.uz/test.php'}
                files = [

                ]
                headers = {
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQzNDcsInJvbGUiOm51bGwsImRhdGEiOnsiaWQiOjQzNDcsIm5hbWUiOiJYYXlpdGJveWV2IEVsYmVram9uIEltaW5qb24gbydnJ2xpIiwiZW1haWwiOiJiYWNrZW5kZGV2b2xwbWVudEBnbWFpbC5jb20iLCJyb2xlIjpudWxsLCJhcGlfdG9rZW4iOm51bGwsInN0YXR1cyI6ImFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJ1Y2VsbF9wcmljZSI6MTE1LCJ0ZXN0X3VjZWxsX3ByaWNlIjpudWxsLCJiYWxhbmNlIjo0NDcwLCJpc192aXAiOjAsImhvc3QiOiJzZXJ2ZXIxIiwiY3JlYXRlZF9hdCI6IjIwMjMtMDctMDFUMTI6MzQ6MjQuMDAwMDAwWiIsInVwZGF0ZWRfYXQiOiIyMDIzLTEwLTAzVDExOjQ0OjA1LjAwMDAwMFoiLCJ3aGl0ZWxpc3QiOm51bGwsImhhc19wZXJmZWN0dW0iOjAsImJlZWxpbmVfcHJpY2UiOjUwfSwiaWF0IjoxNjk2Mzk1MjcxLCJleHAiOjE2OTg5ODcyNzF9.itL7SgwdeOLM3vRdNOtn-rIBtOcn63KNr663cEYwidg'
                }

                response = requests.request("POST", url, headers=headers, data=payload, files=files)
            return render(request, 'sms_muvafaqiyatli.html')

        return redirect('/adminlogin/')


class Imkoniyatlar(View):
    def get(self, request):
        mentor = Teacher_table.objects.all()
        data = {
            'mentor': mentor
        }
        return render(request, 'index_user_admin.html', data)

    def post(self, request):
        if request.user.is_authenticated:
            ReklamaMentor.objects.create(
                teacher_fk=Teacher_table.objects.get(id=request.POST.get(id='mentor')),
                rasm=request.POST.get('file'),
                tarif=request.POST.get('tarif')
            )
            return redirect('/asosiy/IndexAdmin/')
        return redirect('/adminlogin/')


# ----------------------------------------------------------------------------------------------------------------------

class IndexAll(View):
    def get(self, request):
        mentor = Teacher_table.objects.all().count()
        kurslar = Kurs.objects.all().count()
        talabalar = Asosiy_talabalar_safi.objects.all().count()

        data = {
            'mentor': mentor,
            'kurslar': kurslar,
            'talabalar': talabalar,
            'mentorreklama': ReklamaMentor.objects.all(),
            'alooquvchi': ReklamaAlochiOquvchilar.objects.all()[:3],
            'info': Info.objects.all()[::-1]

        }
        return render(request, 'indexuser.html', data)


def IndexDell(request, pk):
    if request.user.is_authenticated:
        Info.objects.get(id=pk).delete()
        return redirect('/asosiy/foydalanuvchiSahifasi/')
    return redirect('/adminlogin/')


class AllLoginPage(View):
    def get(self, request):
        return render(request, 'index.html')


class OquvchiKursgaYozilish(View):
    def get(self, request):
        kurslar = Kurs.objects.all()
        data = {
            'kurslar': kurslar
        }
        return render(request, 'indexform.html', data)

    def post(self, request):
        ismm = request.POST.get('ism')
        famm = request.POST.get('fam')
        tell = request.POST.get('tel')
        kurss = request.POST.get('kurs')
        Sorov.objects.create(
            ism=ismm,
            fam=famm,
            tel=tell,
            kurs_fk=Kurs.objects.get(id=kurss)
        )
        return render(request, 'sorov_muvofiqiyatli.html')


# ______________________________________________________________________________________
# sayt sozlamalari
# ______________________________________________________________________________________

class FoydalanuvchiSahifasi(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'sahifa': Info.objects.all()
            }
            return render(request, 'Foydalanuvchi_sahifasi.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Info.objects.create(
                shirif_matn=request.POST.get('shirif_matn'),
                joylashuv=request.POST.get('joylashuv'),
                tel=request.POST.get('tel'),
                quyi_matn=request.POST.get('quyi_matn'),
                tarif=request.POST.get('tarif'),
            )
            return redirect('/asosiy/foydalanuvchiSahifasi/')
        return redirect('/adminlogin/')


class ReklamaMentorr(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'mentor': Teacher_table.objects.all(),
                'reklamaMentor': ReklamaMentor.objects.all()
            }
            return render(request, "Foalo'qituvchilar.html", data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            ReklamaMentor.objects.create(
                teacher_fk=Teacher_table.objects.get(id=request.POST.get('mentor')),
                rasm=request.FILES.get('rasm'),
                tarif=request.POST.get('tarif'),
                soha=request.POST.get('soha'),
            )
            return redirect('/asosiy/reklamamentor/')
        return redirect('/adminlogin/')


def MentorDelete(request, pk):
    if request.user.is_authenticated:
        ReklamaMentor.objects.get(id=pk).delete()
        return redirect('/asosiy/reklamamentor/')
    return redirect('/adminlogin/')


class YangiliklarIndex(View):
    def get(self, request):
        data = {
            'yangiliklar': Yangiliklar.objects.all()
        }
        return render(request, 'new_index.html', data)


class Imtihonlarr(View):
    def get(self, request):
        data = {
            'elonlar': Elonlar.objects.all()
        }
        return render(request, 'indexexem.html', data)


class ReklamaOquvchilar(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'alooquvchi': ReklamaAlochiOquvchilar.objects.all()
            }
            return render(request, 'natijaliTalabalar.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            ReklamaAlochiOquvchilar.objects.create(
                ism=request.POST.get('ism'),
                fam=request.POST.get('fam'),
                tarif=request.POST.get('tarif'),
                rasm=request.FILES.get('rasm'),
                sertifikat=request.POST.get('ser'),
                facebook=request.POST.get('fb'),
                telegram=request.POST.get('tg'),
                instagram=request.POST.get('ins'),
                youtube=request.POST.get('yt'),
            )
            return redirect('/asosiy/reklamaoquvchilar/')
        return redirect('/adminlogin/')


def ReklamaOquvchiDel(request, pk):
    if request.user.is_authenticated:
        ReklamaAlochiOquvchilar.objects.get(id=pk).delete()
        return redirect('/asosiy/reklamaoquvchilar/')
    return redirect('/adminlogin/')


class Yangiliklarr(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'yangiliklar': Yangiliklar.objects.all()
            }
            return render(request, 'Yangliklar_admin.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Yangiliklar.objects.create(
                nom=request.POST.get('nom'),
                text=request.POST.get('tarif'),
                rasm=request.FILES.get('rasm')
            )
            return redirect('/asosiy/yangiliklarSayt/')
        return redirect('/adminlogin/')


def YangiliklarDel(request, pk):
    if request.user.is_authenticated:
        Yangiliklar.objects.get(id=pk).delete()
        return redirect('/asosiy/yangiliklarSayt/')
    return redirect('/adminlogin/')


class ElonlarSayt(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'elonlar': Elonlar.objects.all()
            }
            return render(request, 'elonlar_admin.html', data)
        return redirect('/adminlogin/')

    def post(self, request):
        if request.user.is_authenticated:
            Elonlar.objects.create(
                nom=request.POST.get('nom'),
                tarif=request.POST.get('tarif'),
                boshlanish_vaqti=request.POST.get('vaqt'),
            )
            return redirect('/asosiy/elonlarSayt/')
        return redirect('/adminlogin/')


def ElonSytDel(request, pk):
    if request.user.is_authenticated:
        Elonlar.objects.get(id=pk).delete()
        return redirect('/asosiy/elonlarSayt/')
    return redirect('/adminlogin/')
