from django.urls import path ,include
from .views import *
urlpatterns = [
    path('IndexAdmin/',IndexAdmin.as_view()),
    path('kurslar/',Kurslar.as_view()),
    path('kursdelete/<int:son>',KursDelete.as_view()),
    path('guruhlar/',Guruhlar.as_view()),
    path('sorov/',Sorovlar.as_view()),
    path('kutayotganlar/',Kutayotganlar.as_view()),
    path('guruhdelete/<int:son>',GuruhDelete.as_view()),
    path('sinov/',Sinovv.as_view()),
    path('talabalar/',Talabalar.as_view()),
    path('davomat/',DavomatAdmin.as_view()),
    path('hujat/',Hujat.as_view()),
    path('teacher/',Teacher.as_view()),
    path('dars/',Dars.as_view()),
    path('sorovdelete/<int:pk>',SorovDelete),
    path('kutushdelete/<int:pk>',KutushDelete),
    path('sinovdelete/<int:pk>',SinovDelete),
    path('talabadelete/<int:pk>',TalabaDelete),
    path('teacherdelete/<int:pk>',TeacherDelete),

]