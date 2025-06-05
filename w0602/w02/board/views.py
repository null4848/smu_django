from django.shortcuts import render, redirect
from board.models import Board
# Create your views here.

def write(request):    
    if request.method == 'GET':
        return render(request, 'board/write.html')
    elif request.method == 'POST':
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)

        qs.bno = qs.bgroup
        qs.save()
        print("데이터 확인 : ", id, btitle, bfile)
        print("데이터 추가 : ", qs.bgroup, qs.bstep, bfile)
        
        return redirect('board:list')

def list(request):
    qs = Board.objects.all()
    context = {'list':qs}
    return render(request, 'board/list.html', context)