# investigations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.investigation_list, name='investigation_list'),
    path('start/', views.start_investigation, name='start_investigation'),
    path('<int:investigation_id>/', views.investigation_detail, name='investigation_detail'),
]
