from django.urls import re_path
from polls import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    re_path(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    re_path(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
]