from django.shortcuts import render, redirect
from member.models import Member


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("아이디, 패스워드 : ",id,pw)
        
        try:
            txt = 1
        except:
            txt = 0
            
    
    
    return render(request, 'member/login.html')