from django.shortcuts import render
import requests
import json

dlist = []
# Create your views here.
def list(request):
    global dlist
    key = '73f817d94dff0faf42032fd8f09bb219'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt=20250617'
    response = requests.get(url)
    json_data = json.loads(response.text)
    dlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    print("10개 : ",dlist )
    context = {"list":dlist}
    return render(request, 'pboard3/list.html', context)

def view(request, rank):
    global dlist
    print("넘어온 rank", rank)
    
    context = {}
    for d in dlist:
        if d['rank']==str(rank):
            context['dData']=d
            
    print(context['dData'])
        
    return render(request, 'pboard3/view.html', context)