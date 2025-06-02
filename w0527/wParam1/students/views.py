from django.shortcuts import render

# Create your views here.
def result(request):
    id = request.GET.get('id')
    pw = request.GET.get('pw')
    name = request.GET.get('name')
    context={'id':id,'pw':pw,'name':name}
    return render(request, 'students/result.html', context)