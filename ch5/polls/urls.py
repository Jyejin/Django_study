from django.urls import re_path
from polls import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    re_path(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),
]