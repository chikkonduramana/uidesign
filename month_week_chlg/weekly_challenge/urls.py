from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_week,name = 'index_week'),
    path('<week_name>/', views.week_challenge, name = 'week_challenge') 
]