from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리


# get, post
def view(request):
    # html에서 데이터 전송
    id = request.POST.get('id')
    name = request.POST.get('name')
    # 데이터를 html 전송
    context = {"id":id,"pw":name}
    return render(request,'board/view.html', context)

# ajax 전송 방식 - get, post 
def view2(request):
    # html에서 데이터 전ekf
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    
    # QuerySet, QueryList -> list 타입
    # models db데이터가 있으면, list 타입으로 변경 후 전송해야 함
    
    # 데이터를 html 전송
    context = {"id":id,"pw":name}
    return JsonResponse(context)
    
def list(request):
    return render(request,'board/list.html')