from django.db import models
from django.utils import timezone #아까 시간대 설정한거 / 게시일이나 생성일

class Post(models.Model): #클래스로 관리함 / 위에 import models의 Model을 상속받음
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #외래키
    title = models.CharField(max_length=200)#제목을 200으로 제한
    text = models.TextField() #200자 이상쓸때
    created_date = models.DateTimeField(default=timezone.now) #만들었을때 / defalt는 현재로 /날짜, 시간 저장
    published_date = models.DateTimeField(blank=True, null=True) #null값 허용

    def publish(self):
        self.published_date=timezone.now() #등록버튼 눌렀을때
        self.save()

    def __str__(self):
        return self.title

