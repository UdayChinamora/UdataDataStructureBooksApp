from django.shortcuts import render
from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home-page'),
    path('my_books/', views.my_books, name='my_books'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('linked_list_books/ ', views.linked_list_books, name='linked_list_books'),
    path('sorted_book_list/', views.sorted_book_list, name='sorted_book_list'),
    path('enqueue_view/', views.enqueue_view, name='enqueue_view'),
    path('map_book_list/', views.map_book_list, name='map_book_list'),
    path('edited_book_list/', views.edited_book_list, name='edited_book_list'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('queue_book_view/', views.queue_book_view, name='queue_book_view'),
    path('search_books/', views.search_books, name='search_books'),





]
