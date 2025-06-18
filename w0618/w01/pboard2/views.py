from django.shortcuts import render
import requests 
import json

### 전역 변수
dlist = [] # list 함수에서 공공데이터를 가지고 와서 view 함수에 전달

# 공공데이터 리스트
def list(request):
    global dlist # 전역변수 사용
    
    # 공데이터 가져오기에 필요한 정보
    pageNo = 1
    serviceKey='ccbwa2a%2Fgupb23PWffSQbJTaeZ%2B3NjEPrf%2F4WVV%2FwsouzGFTlHT%2BN85izwlRyCvGa12etsaGXs55YTiSvdJiVg%3D%3D'   
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={serviceKey}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    
    # 공공데이터 가져오기
    response = requests.get(url)          # 공공데이터 가져온 타입 : str타입
    json_data = json.loads(response.text)  # json타입으로 변경 -> dict타입
    # 필요한 데이터, 리스트로 변경해서 전달
    dlist = json_data['response']['body']['items']['item']
    print("10개 : ",dlist)
    
    context = {'list':dlist}
    return render(request,'pboard2/list.html',context)

## 공공데이터 상세보기
def view(request, galContentId):
    global dlist
    print("넘어온 galContentId : ",galContentId)
    
    context = {}
    for d in dlist:
        if d['galContentId'] ==str(galContentId):
            context['dData'] = d
            
    print(context['dData'])
    return render(request, 'pboard2/view.html', context)