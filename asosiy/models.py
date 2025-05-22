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
        return f"{self.guruh_nom}"


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
    file=models.FileField(upload_to='hujat')
    tarif=models.TextField(null=True,blank=True)
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



class Darslar(models.Model):
    kurs_fk = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    guruh_fk = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    teacher_fk = models.ForeignKey(Teacher_table, on_delete=models.CASCADE)
    hafta_kunlari=models.CharField(max_length=50,null=True,blank=True) #juft toq
    dars_boshlanish_vaqti=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.guruh_fk} | {self.teacher_fk}"


class Tolov(models.Model):
    asosiy_talabalar_safi_fk=models.ForeignKey(Asosiy_talabalar_safi,on_delete=models.CASCADE)
    summa=models.IntegerField()
    vaqt=models.DateTimeField(auto_now_add=True)
    tolov_qilgan_shaxs=models.CharField(max_length=60)
    tolov_qilgan_shaxs_tel=models.CharField(max_length=13,null=True,blank=True)
    def __str__(self):
        return f"{self.asosiy_talabalar_safi_fk} | {self.summa}"

class Umumiy_shot(models.Model):
    asosiy_talabalar_safi_fk = models.ForeignKey(Asosiy_talabalar_safi, on_delete=models.CASCADE)
    umumiy_summa = models.IntegerField()
    def __str__(self):
        return f"{self.asosiy_talabalar_safi_fk} | {self.umumiy_summa}"
class Kurs_summa(models.Model):
    kurs_fk=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    summa=models.SmallIntegerField()
    def __str__(self):
        return f"{self.kurs_fk} | {self.summa}"
class Yechib_olish(models.Model):
    oy_nomi=models.CharField(max_length=60)
    kurs_fk = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    asosiy_talabalar_safi_fk=models.ForeignKey(Asosiy_talabalar_safi,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.oy_nomi} | {self.asosiy_talabalar_safi_fk}"

class Harajat(models.Model):
    harajat_turi=models.CharField(max_length=50)
    summa=models.IntegerField()
    tarif=models.TextField()
    vaqt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.harajat_turi} {self.summa}"
class Mentor_oylik(models.Model):
    mentor_fk=models.ForeignKey(Teacher_table,on_delete=models.CASCADE)
    oy_nomi=models.CharField(max_length=25)
    summa=models.IntegerField()
    vaqt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mentor_fk} {self.summa}"

# ------------------------------------------------------------------------------------------------------------

class ReklamaMentor(models.Model):
    teacher_fk=models.ForeignKey(Teacher_table,on_delete=models.CASCADE)
    rasm=models.FileField(upload_to='reklama_mentor_rasmlari/')
    tarif=models.TextField()
    soha = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return f"{self.teacher_fk}"

class ReklamaAlochiOquvchilar(models.Model):
    ism=models.CharField(max_length=25)
    fam=models.CharField(max_length=25)
    tarif=models.TextField()
    rasm=models.FileField(upload_to='talaba_rasm')
    sertifikat=models.FileField(upload_to='sertifikatlar',blank=True,null=True)
    facebook=models.URLField(blank=True,null=True)
    telegram=models.URLField(blank=True,null=True)
    instagram=models.URLField(blank=True,null=True)
    youtube=models.URLField(blank=True,null=True)

    def __str__(self):
        return f"{self.ism} {self.fam}"

class Yangiliklar(models.Model):
    nom=models.CharField(max_length=100)
    text=models.TextField()
    rasm=models.FileField(upload_to='yangiliklar_rasm')
    vaqt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nom}"
class Elonlar(models.Model):
    nom=models.CharField(max_length=100)
    tarif=models.TextField()
    boshlanish_vaqti=models.DateField()
    def __str__(self):
        return f"{self.nom}"

class Info(models.Model):
    shirif_matn=models.TextField(null=True,blank=True)
    joylashuv=models.CharField(max_length=50)
    tel=models.CharField(max_length=13)
    quyi_matn=models.CharField(max_length=50)
    tarif=models.TextField(null=True,blank=True)