from django.shortcuts import render

# Create your views here.
def step01(request):
    return render(request,'member/step01.html')
