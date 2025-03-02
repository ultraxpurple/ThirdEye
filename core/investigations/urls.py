# investigations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.investigation_list, name='investigation_list'),
    path('start/', views.start_investigation, name='start_investigation'),
    path('<int:investigation_id>/', views.investigation_detail, name='investigation_detail'),
    path('<int:investigation_id>/download/', views.download_report, name='download_report'),
    path('<int:investigation_id>/rename/', views.rename_report, name='rename_report'),
    path('<int:investigation_id>/delete/', views.delete_report, name='delete_report'),
]
