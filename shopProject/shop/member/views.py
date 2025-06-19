from django.shortcuts import render,redirect
from django.http import JsonResponse
from member.models import Member
import random
import numpy as np

### 전역변수
random_txt = ''


# get:로그인페이지, post:로그인확인
def login(request):
    ## 쿠키정보 가져오기
    cook_id = request.COOKIES.get('cook_id','')
    context = {'cook_id':cook_id}
    if request.method == 'GET':
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        print('넘어온 id,pw,idsave : ',id,pw,idsave)
        ## db확인
        qs = Member.objects.filter(id=id,pw=pw) # None
        print('qs : ',qs)
        if qs:
            msg = 1
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
        else:
            msg = 0    
        context['msg'] = msg
        response = render(request,'member/login.html',context)
        if idsave:
            response.set_cookie('cook_id',id,max_age=60*60*24)
        else:
            response.delete_cookie('cook_id')
        return response
        
# 로그아웃
def logout(request):
    ### 섹션 모두삭제
    request.session.clear()
    msg = 2
    context = {'msg':msg}
    return render(request,'member/login.html',context)

# 회원가입01
def step01(request):
    return render(request,'member/step01.html')

# 이메일발송
def emailSend(request):
    email = request.POST.get('email')
    # 알파벳 26개, 숫자 10개 : 36개  0-35
    txt = 'abcdefghijklmnopqrstuvwxyz0123456789'
    random_array = [] # 초기화
    random_array = np.random.randint(0, 35, 10)
    print('넘어온 email : ',email)
    print('랜덤 rno : ',random_array)
    global random_txt
    for i in random_array:
         random_txt += txt[i]
         
    ### 이메일 발송 부분 추가
    
    ######################     
    context = {'msg':'success','random_txt':random_txt}
    return JsonResponse(context)


# 이메일 랜덤번호 확인
def confirmChk(request):
    confirmTxt = request.POST.get('confirmTxt')
    if random_txt == confirmTxt:
        msg = 'success'
    else:
        msg = 'fail'    
    context = {'msg':msg,'random_txt':random_txt}
    return JsonResponse(context) 