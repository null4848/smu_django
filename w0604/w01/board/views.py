from django.shortcuts import render, redirect
from board.models import Board
# F : 검색된 필드에서 특정 컬럼의 값을 가져올 때 사용
# Q : and, or, not 연산 이용시 사용
from django.db.models import F, Q
from django.core.paginator import Paginator

# 게시판 리스트 - 일반 게시판 리스트, 검색 게시파 ㄴ리스
def list(request):
    # ㅎ현재 페이지 int 병경
    page = int(request.GET.get('page', 1)) # 없을 때 1페이지로 넘겨줌
    
    # serach로 넘어올때
    search = request.GET.get('search','')
    category = request.GET.get('category','')
    print("검색데이터 : ", category, search)
    
    if search == '':
        # 게시글 전체 가져오기
        qs = Board.objects.order_by('-bgroup', 'bstep')
        
        # 페이지 분기
        paginator = Paginator(qs, 20) 
        list = paginator.get_page(page)
        context = {"list":list, 'page':page}
        return render(request, 'board/list.html', context)
    
    else: # 검색으로 넘어ㄱ온 경우
        # 게시글 전체 가져오기 and:& or:| not:~
        if category == 'all':
            qs = Board.objects.filter(
                Q(btitle__contains=search) | Q(bcontent__contains=search))
        elif category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        else:
            qs = Board.objects.filter(bcontent__contains=search)
            
        # 페이지 분기
        paginator = Paginator(qs, 20) 
        list = paginator.get_page(page)
        context = {"list":list, 'page':page, 'search':search, "category":category}
        return render(request, 'board/list.html', context)

# 게시글 보기
def view(request, bno):
    # qs = Board.objects.get(bno=bno)
    # 1. qs값 수정
    # qs.bhit += 1
    # qs.save()
    
    # 2. F함수 사용 - filter 검색 후 qs에서 특정컬럼의 값을 가져오는 함수
    category = request.GET.get('category', '')
    search = request.GET.get('search','')
    
    qs = Board.objects.filter(bno=bno)
    qs.update(bhit = F('bhit')+1) # save까지 됨
    context = {'board':qs[0], 'category':category, 'search':search}
    
    return render(request, 'board/view.html', context)

# 게시글 쓰기 - 게시글 페이지 열기, 게시글 저장
def write(request):
    if request.method=='GET':
        return render(request, 'board/write.html')
    elif request.method=='POST':
        id = request.POST.get('id') # 섹션에서 가져옴
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print('가져온 데이터 : ', id, btitle, bcontent, bfile)
        
        # 1. save() 저장
        # Board(id=id, btitle=btitle, bcontent=bcontent, bfile=bfile).save()
        # 2. create 저장
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        
        context={'msg':1}
        
        return render(request, 'board/write.html', context)

# 게시글 수정 
def update(request, bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {"board":qs}
        return render(request, 'board/update.html', context)
    
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        # qs.bfile = bfile
        qs.save()
        
        context = {"msg":1, 'board':qs}
        return render(request, 'board/update.html', context)

# 게시글 삭제
def delete(request, bno):
    ## 게시글 삭제
    Board.objects.get(bno=bno).delete()
    return redirect('/board/list/')

# 답글 달기
def reply(request, bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request, 'board/reply.html', context)
    
    elif request.method == 'POST':
        id = request.POST.get('id') # sessoin_id 가져옴.
        bgroup = request.POST.get('bgroup') # 부모의 bgroup
        bstep = int(request.POST.get('bstep')) # 부모의 bstep
        bindent = int(request.POST.get('bindent')) # 부모의 bindent
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        ## 답글 달기 저장
        # 1. gt, lt, gte, lte(작거나 같다) 언더바 두개
        # 모든 자식들은 전부 bstep을 1씩 증가시켜야 함.
        # 부모보다 bstep 더 큰 것, 전부 bstep 1씩 증가 
        # F 함수 현재 찾아진 컬럼의 값을 모두 가져옴.
        reply_qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
        reply_qs.update(bstep = F('bstep')+1)
        
        # 2. db 저장
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1, bfile=bfile)
        print('')
        
        context = {"msg":1, "board":qs}
        return render(request, 'board/reply.html', context)
        