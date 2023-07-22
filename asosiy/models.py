from django.db import models
from django.contrib.auth.models import User


# Adminstrator uchun tables
class Kurs(models.Model):
    nom=models.CharField(max_length=30)
    ochilgan_sana=models.DateField()
    def __str__(self):
        return f"{self.nom}"


class Sorov(models.Model):
    ism=models.CharField(max_length=30)
    fam=models.CharField(max_length=30)
    tel=models.CharField(max_length=13)
    kurs_fk=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    sorov_qoldirilgan_vaqt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.ism} {self.fam} | {self.kurs_fk}"


class Guruh(models.Model):
    kurs_fk=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    guruh_nom=models.CharField(max_length=50)
    ochilgan_sana=models.DateField()
    davomiyligi=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.kurs_fk} | {self.guruh_nom}"


class Kutish(models.Model):
    sorov_fk=models.ForeignKey(Sorov,on_delete=models.CASCADE)
    batafsil=models.TextField()
    def __str__(self):
        return f'{self.sorov_fk}'


class Sinov(models.Model):
    kutish_fk = models.ForeignKey(Kutish, on_delete=models.CASCADE,null=True,blank=True)
    kurs_fk = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    guruh_fk = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    vaqt=models.DateField(null=True,blank=True)
    def __str__(self):
        return f'{self.kurs_fk} | {self.guruh_fk}'


class Asosiy_talabalar_safi(models.Model):
    ism=models.CharField(max_length=35)
    fam=models.CharField(max_length=50)
    tel_1=models.CharField(max_length=13)
    tel_2=models.CharField(max_length=13)
    rasm=models.FileField(null=True,blank=True)
    tugulgan_joy=models.CharField(max_length=60)
    tugulgan_sana=models.DateField()
    kurs_fk = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    guruh_fk = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism} {self.fam}"


class Hujatlar(models.Model):
    nom=models.CharField(max_length=100)
    file=models.FileField()
    def __str__(self):
        return f"{self.nom}"


class Teacher_table(models.Model):
    ism = models.CharField(max_length=35)
    fam = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    manzil=models.CharField(max_length=60)
    tugulgan_sana = models.DateField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism} {self.fam}"


# class Adminstrator(models.Model):
#     ism = models.CharField(max_length=35)
#     fam = models.CharField(max_length=50)
#     tel = models.CharField(max_length=13)
#     manzil=models.CharField(max_length=60)
#     tugulgan_sana = models.DateField()
#
#     def __str__(self):
#         return f"{self.ism} {self.fam}"


class Darslar(models.Model):
    kurs_fk = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    guruh_fk = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    teacher_fk = models.ForeignKey(Teacher_table, on_delete=models.CASCADE)
    hafta_kunlari=models.CharField(max_length=50,null=True,blank=True) #juft toq
    dars_boshlanish_vaqti=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.guruh_fk} | {self.teacher_fk}"


# class Tolov(models.Model):
#     asosiy_talabalar_safi_fk=models.ForeignKey(Asosiy_talabalar_safi,on_delete=models.CASCADE)
#     oy=models.CharField(max_length=15)
#     summa=models.IntegerField()
#     chegirma=models.PositiveIntegerField(default=0)
#     tolov_qilindi=models.BooleanField(default=False)
#     adminstrator_fk=models.ForeignKey(Adminstrator,on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.asosiy_talabalar_safi_fk} | {self.oy}"

# ------------------------------------------------------------------------------------------------------------



