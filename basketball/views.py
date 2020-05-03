from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'basketball/home.html')

@login_required
def tournament(request):
    return render(request, 'basketball/tournament.html')

@login_required
def about_us(request):
    return render(request, 'basketball/about_us.html')

@login_required
def faq(request):
    return render(request, 'basketball/faq.html')     

