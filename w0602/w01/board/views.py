from django.shortcuts import render

# Create your views here.
# 게시판 글쓰기 리스트
def list(request):
    return render(request,'board/list.html')

# 쓰기페이지, 쓰기 저장
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print("데이터 확인 : ",btitle,bcontent,bfile)
        
        return render(request,'board/write.html')