from django.urls import re_path
from books import views

urlpatterns = [
    re_path(r'^$', views.BooksModelView.as_view(), name='index'),

    re_path(r'^book/$', views.BookList.as_view(), name='book_list'),
    re_path(r'^author/$', views.AuthorList.as_view(), name='author_list'),
    re_path(r'^publisher/$', views.PublisherList.as_view(), name='publisher_list'),

    re_path(r'^book/(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book_detail'),
    re_path(r'^author/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
    re_path(r'^publisher/(?P<pk>\d+)/$', views.PublisherDetail.as_view(), name='publisher_detail'),
]