from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list(request):
    return HttpResponse('리스트 페이지를 오픈합니다.')
    # return render(request,'list.html')
    
def view(request):
    return HttpResponse('뷰페이지를 오픈합니다.')

def write(request):
    return render(request, 'write.html') # html 페이지 오픈

def delete(request):
    return render(request, 'delete.html') # html 페이지 오픈
