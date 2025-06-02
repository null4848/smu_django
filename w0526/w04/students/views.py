from django.shortcuts import render
from students.models import Student

# Create your views here.
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'list.html', context)