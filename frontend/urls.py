from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login', views.login, name='login'),
    path('complaints/<str:username>', views.complaints, name='complaints'),
    path('register/<str:username>', views.register, name='register'),
]