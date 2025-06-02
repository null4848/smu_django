from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from students.models import Student
from django.urls import reverse

# 학생정보리스트 페이지
def list(request):
    # Student테이블데이터가져오기
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'students/list.html', context)
    # return HttpResponse('txt')
    
# 학생등록페이지    
def write(request):
    return render(request, 'students/write.html')

# 학생등록저장
def write2(request):
    # request.POST[], request.POST.get()
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    print("데이터 정보 :",name,major,grade,age,gender)
    
    qs = Student(name=name, major=major, grade=grade,age=age,gender=gender)
    qs.save()
    return redirect('students:list')
    # return HttpresponseRedirect(recverse('student:list))
    # return render(request, 'students/write.html')