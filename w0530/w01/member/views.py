from django.shortcuts import render, redirect
from member.models import Member

### 로그인 - 페이지 : GET, 로그인 - 확인 : POST
def login(request):
    if request.method == 'GET': # 로그인페이지
        return render(request,'member/login.html')
    elif request.method == 'POST': #로그인확인
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("아이디, 패스워드 : ",id, pw)
        # id,pw가 있는지 확인
        try:
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id'] = id  # session할당
                txt = 1
                # context['success'] = '반갑습니다. 로그인 되었습니다.'
            else:
                txt = -1
                # context['pw_none'] = '비밀번호가 일치하지 않습니다. 다시 입력하세요.'
        except:
            txt = 0
            # context['id_none'] = '아이디가 존재하지 않습니다. 회원가입을 하셔야 로그인이 가능합니다.'
        # try:
        #     qs = Member.objects.get(id=id,pw=pw)
        #     request.session['session_id'] = id  # session할당
        #     txt = 1 # 성공
        # except:
        #     txt = 0 # 실패
        context = {'msg':txt}
        return render(request,'member/login.html',context)
        # return redirect('/')

def logout(request):
    # 세션 삭제
    request.session.clear()
    context = {'msg':2}
    
    # context = ['logout']
    return render(request,'member/login.html', context)
