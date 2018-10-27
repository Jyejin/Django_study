#Admin 사이트에 모델 클래스를 등록해주는 파일
#db 변경사항이 생겼다면 makemigrations

from django.contrib import admin
from polls.models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline): #delete checkbox 생김
    model = Choice
    extra = 2 #한 번에 보여지는 choice text 수

class QuestionAdmin(admin.ModelAdmin):
    #필드 분리해서 보여주기
    fieldsets = [
        ('Question Statement', {'fields' : ['question_text']}),
        ('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']}), #collapse => 필드접기
    ]
    #fields = ['pub_date', 'question_text'] #필드 순서 변경!
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date') #레코드 리스트 항목 지정
    list_filter = ['pub_date'] #필터 사이드 바 추가
    search_fields = ['question_text'] #검색 창 추가

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
