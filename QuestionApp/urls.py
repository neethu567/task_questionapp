from django.urls import path,include
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from QuestionApp import views
urlpatterns=[
    # path('questions/', views.question_list),
    # path('questions/<int:pk>/', views.question_detail),
    # path('choice/', views.choice_list),
    # path('choice/<int:pk>/', views.choice_detail),
    # path('choice/votes/<int:pk>/', views.vote)
    path('questions/', views.question_list.as_view()),
    path('questions/<int:pk>/', views.question_detail.as_view()),
    path('choice/', views.choice_list.as_view()),
    path('choice/<int:pk>/', views.choice_detail.as_view()),
    # path('choice/votes/<int:pk>/', views.Vote.as_view())
    path('users/', views.user_list.as_view()),
    path('users/<int:pk>/', views.user_detail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += [
#     path('login/', include('rest_framework.urls')),
# ]