from django.urls import path

from . import views

app_name = 'chats'
urlpatterns = [
    path('', views.index, name='index'),
    path('thread/<int:thread_id>', views.show_thread, name='show_thread'),
    path('create_thread/', views.create_thread, name='create_thread'),
    path('create_reply/<int:thread_id>', views.create_reply, name='create_reply'),

]
