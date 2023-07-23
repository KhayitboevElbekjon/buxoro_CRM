from django.urls import path ,include
from .views import *
urlpatterns = [
    path('mentorlogin/',Mentorlogin.as_view()),
    path('indexteacher/',IndexTeacher.as_view()),

]