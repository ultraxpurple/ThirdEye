# investigations/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Investigation

def start_investigation(request):
    return HttpResponse("Start investigation placeholder")

def investigation_detail(request, investigation_id):
    return HttpResponse(f"Investigation detail for investigation {investigation_id}")

def investigation_list(request):
    # Fetch investigations (which include report information)
    investigations = Investigation.objects.filter(user=request.user)
    return render(request, 'investigations/investigation_list.html', {'investigations': investigations})

def download_report(request, investigation_id):
    return HttpResponse(f"Download report for investigation {investigation_id}")

def rename_report(request, investigation_id):
    return HttpResponse(f"Rename report for investigation {investigation_id}")

def delete_report(request, investigation_id):
    return HttpResponse(f"Delete report for investigation {investigation_id}")
