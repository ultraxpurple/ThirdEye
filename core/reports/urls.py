# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('view/<int:report_id>/', views.view_report, name='view_report'),
    path('download/<int:report_id>/', views.download_report, name='download_report'),
    path('rename/<int:report_id>/', views.rename_report, name='rename_report'),
    path('delete/<int:report_id>/', views.delete_report, name='delete_report'),
]
