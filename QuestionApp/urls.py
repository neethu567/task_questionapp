from django.urls import path
from QuestionApp import views
urlpatterns=[
    path('questions/', views.question_list),
    path('questions/<int:pk>/', views.question_detail),
    path('choice/', views.choice_list),
    path('choice/<int:pk>/', views.choice_detail),
]