from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', include('asosiy.urls')),
    path('mentor/', include('mentor.urls')),
    path('adminlogin/',AdminLogin.as_view()),
    path('logout/',logautview)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
