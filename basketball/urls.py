from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('tournaments/', views.tournament, name='tournament'),
    path('about_us/', views.about_us, name='about'),
    path('faq/', views.faq, name='faq'),
]
