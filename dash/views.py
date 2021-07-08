from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'dash/dashboard.html')

def billing(request):
    return render(request, 'dash/billing.html')
def profile(request):
    return render(request, 'dash/profile.html')
def signin(request):
    return render(request, 'dash/signin.html')
def signup(request):
    return render(request, 'dash/signup.html')
def tables(request):
    return render(request, 'dash/tables.html')
def vr(request):
    return render(request, 'dash/virtualreality.html')
