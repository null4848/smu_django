from django.shortcuts import render
from member.models import Member

# Create your views here.
def login(request):
    if request.method == 'GET':
        
        print("모든 쿠키 : ",request.COOKIES)
        
        idCheck = request.COOKIES.get('idCheck', '')
        context = {'save_id':idCheck}
        
        return render(request, 'member/login.html', context)
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idCheck = request.POST.get('idCheck')
        
        try:
            qs = Member.objects.all(id=id, pw=pw)
        
        except:
            context = {'msg':0}
            response = render(request, 'member')
            
            
        return render(request, 'member/login.html')

def join01(request):
    return render(request, 'member/join01.html')

def join02(request):
    return render(request, 'member/join02.html')

def join03(request):
    return render(request, 'member/join03.html')