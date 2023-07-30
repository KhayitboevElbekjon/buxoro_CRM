from django.urls import path ,include
from .views import *
urlpatterns = [
    path('mentorlogin/',Mentorlogin.as_view()),
    path('indexteacher/',IndexTeacher.as_view()),
    path('guruh/',GuruhlarView.as_view()),
    path('reja/',Reja.as_view()),
    path('rejadelete/<int:pk>',RejaDelete),
    path('davomatt/<str:pk>',Davomatt.as_view()),
    path('uzlashtirish/<str:pk>',Ozlashtirish.as_view()),
    path('konfensiya/',Konfrensiyaa.as_view()),
    path('konfrensiyadelete/<int:pk>',KonfrensiyaDelete),
    path('bitatalaba/<int:pk>',BittaTalaba.as_view()),
    path('saqlamalar/',Saqlanmalar.as_view())

]