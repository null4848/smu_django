from django.db import models
from member.models import Member

# Create your models here.

# Create your models here.
class Board(models.Model):
    bno = models.AutoField(primary_key=True) # 기본키 등록
    # 외래키(Foreign Key)
    member = models.ForeignKey(Member,on_delete=models.SET_NULL, null=True)
    # id = models.CharField(max_length=100) # 작성자
    # member = models.ForeignKey(Member,on_delete=models.CASCADE)
    btitle = models.CharField(max_length=1000) # 제목
    bcontent = models.TextField() # 내용
    # 답글 달기 사용
    bgroup = models.IntegerField(default=0) # 답글달기 묶음
    bstep = models.IntegerField(default=0) 
    bindent = models.IntegerField(default=0)
    # ---
    bhit = models.IntegerField(default=0) # 조회수
    bfile = models.ImageField(max_length=100, null=True, blank=True, upload_to='board') # 이미지 파일 
    # FileField : 모든 파일 업로드 가능
    ntchk = models.IntegerField(default=0)
    bdate = models.DateTimeField(auto_now=True) # 현재날짜시간자동등록
    
    def __str__(self):
        return f"{self.bno}, {self.btitle}, {self.bgroup}"
    