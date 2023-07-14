from django.db import models
# from asosiy.models import *

from asosiy.models import Guruh,Asosiy_talabalar_safi


class Mavzu(models.Model):
    nom=models.CharField(max_length=50)
    link=models.CharField(max_length=100000)
    description=models.TextField()
    vaqt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nom}"


class Davomat(models.Model):
    mavzu_fk=models.ForeignKey(Mavzu,on_delete=models.CASCADE)
    guruh_fk=models.ForeignKey(Guruh,on_delete=models.CASCADE)
    asosiy_talabalar_safi_fk=models.ForeignKey(Asosiy_talabalar_safi,on_delete=models.CASCADE)
    darsga_qatnashdi=models.BooleanField(default=False)
    vaqt=models.DateTimeField()
    def __str__(self):
        return f"{self.asosiy_talabalar_safi_fk}"


class Konfrensiya(models.Model):
    batafsil=models.CharField(max_length=60)
    link=models.CharField(max_length=100000)
    guruh=models.ManyToManyField(Guruh)
    vaqt=models.DateTimeField()
    def __str__(self):
        return f"{self.batafsil}"


# class Post(models.Model):
#     matn=models.TextField()
#     vaqt=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.matn}"


class Baholash(models.Model):
    mavzu_fk=models.ForeignKey(Mavzu,on_delete=models.CASCADE)
    guruh_fk=models.ForeignKey(Guruh,on_delete=models.CASCADE)
    asosiy_talabalar_safi_fk=models.ForeignKey(Asosiy_talabalar_safi,on_delete=models.CASCADE)
    min_ball=models.SmallIntegerField()
    max_ball=models.SmallIntegerField()
    def __str__(self):
        return f"{self.asosiy_talabalar_safi_fk}"