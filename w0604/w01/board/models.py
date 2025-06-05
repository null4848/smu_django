from django.db import models

# Create your models here.
class Board(models.Model):
    bno = models.AutoField(primary_key=True) # 기본키 등록
    id = models.CharField(max_length=100) # 작성자
    btitle = models.CharField(max_length=1000) # 제목
    bcontent = models.TextField() # 내용
    # 답글 달기 사용
    bgroup = models.IntegerField(default=0) # 답글달기 묶음
    bstep = models.IntegerField(default=0) 
    bindent = models.IntegerField(default=0)
    # ---
    bhit = models.IntegerField(default=0)
    bfile = models.ImageField(max_length=100, null=True, blank=True, upload_to='board')
    # FileField : 모든 파일 업로드 가능
    bdate = models.DateTimeField(auto_now=True) # 현재날짜시간자동등록
    
    def __str__(self):
        return f"{self.bno}, {self.btitle}, {self.bgroup}"
    