from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<month_name>/', views.get_challenge, name = 'get_challenge')
]