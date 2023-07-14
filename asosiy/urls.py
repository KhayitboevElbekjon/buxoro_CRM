from django.urls import path ,include
from .views import *
urlpatterns = [
    path('IndexAdmin/',IndexAdmin.as_view()),
    path('kurslar/',Kurslar.as_view()),
    path('kursdelete/<int:son>',KursDelete.as_view()),
    path('guruhlar/',Guruhlar.as_view())

]