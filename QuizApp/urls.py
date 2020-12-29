from django.contrib import admin
from django.urls import path
from quiz import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name = 'welcome'),
    path('quiz/', views.quiz, name = 'quiz'),
    path('result/', views.result, name = 'result'),
    path('save_ans/', views.save_ans, name = 'saved_answer'),
]
