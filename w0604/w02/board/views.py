from django.shortcuts import render
from board.models import Board

# Create your views here.
def list(request):
    qs = Board.objects.order_by('-bno','bstep')
    context = {"list":qs}
    return render(request, 'board/list.html', context)

def write(request):
    if request.method=='GET':
        return render(request, 'board/write.html')
    elif request.method=='POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print(id, btitle, bcontent, bfile)
        
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bfile=bfile)
        qs.bgroup=qs.bno
        qs.save()
        
        context = {"msg":1}
        
        return render(request, 'board/write.html', context)