from django.shortcuts import render

# Create your views here.
def result(request, id, pw, name):
    context={'id':id, 'pw':pw, 'name':name}
    return render(request, 'students/result.html', context)