from django.shortcuts import render

def koyambedu(request):
    return render(request,'koyambedumarket/koyambedu.html')
def vegmarket(request):
    return render(request,'koyambedumarket/vegmarket.html')
def metro(request):
    return render(request,'koyambedumarket/metro.html')
def sewage(request):
    return render(request,'koyambedumarket/sewage.html')
def busstand(request):
    return render(request,'koyambedumarket/busstand.html')
def flower(request):
    return render(request,'koyambedumarket/flower.html')

# Create your views here.
