from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,'list.html')

def write(request):
    return render(request,'write.html')

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')