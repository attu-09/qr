from django.urls import path
from .views import *
urlpatterns=[
    path("",scanner),
    path('success',success,name='success'),
    path('adm',admin,name='admin'),
    path('login',login,name='login'),
    path('adm/logout',logout),
]
