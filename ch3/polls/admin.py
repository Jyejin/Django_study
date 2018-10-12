#Admin 사이트에 모델 클래스를 등록해주는 파일
#db 변경사항이 생겼다면 makemigrations

from django.contrib import admin
from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

