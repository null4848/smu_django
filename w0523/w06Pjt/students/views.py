from django.shortcuts import render

# Create your views here.

def list(request):
    # qs = S
    return render(request, 'list.html')

def view(request):
    return render(request,'view.html')