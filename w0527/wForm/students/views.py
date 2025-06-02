from django.shortcuts import render

# Create your views here.
def write(request):
    return render(request, 'write.html')

def result(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    context ={'id':id, 'pw':pw, 'name':name, 'gender':gender, 'hobbys':hobbys}
    return render(request, 'result.html', context)