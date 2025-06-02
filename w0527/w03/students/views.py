from django.shortcuts import render

# Create your views here.
def list(request):
    id = request.POST.get('id') # 변수
    pw = request.POST.get('pw') # 변수
    gender = request.POST.get('gender') # 변수
    hobbys = request.POST.getlist('hobby') # 리스트
    print('입력된 id : ', id)
    print('입력된 pw : ', pw)
    print('입력된 gender : ', gender)
    print('입력된 hobby : ', hobbys)
    context = {'id':id, 'pw':pw, 'gender':gender, 'hobby':hobbys}
    return render(request, 'students/list.html',context)


def view(request):
    #get방식
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름 : ", name)
    print("나이 : ", age)
    context={'name':name, 'age':age}
    return render(request, 'students/view.html', context)

def write(request):
    return render(request, 'students/write.html')

def result(request):
    name = request.POST.get('name')
    kor = request.POST.get('kor')
    eng = request.POST.get('eng')
    total = int(kor)+int(eng)
    hobbys = request.POST.getlist('hobby')
    print("이름 : ",name)
    print("국어 : ",kor)
    print("영어 : ",eng)
    print("합계 : ",total)
    print("취미 : ",hobbys)
    context = {'name':name,'kor':kor,'eng':eng,'total':total,'hobby':hobbys}
    return render(request, 'students/result.html', context)

def send(request, name, age):
    print("전달 받은 값 : ",name,age)
    context = {'name': name, 'age': age}
    return render(request, 'students/send.html', context)
