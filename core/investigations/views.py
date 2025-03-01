# investigations/views.py
from django.http import HttpResponse

def investigation_list(request):
    return HttpResponse("List of investigations")

def start_investigation(request):
    return HttpResponse("Start a new investigation")

def investigation_detail(request, investigation_id):
    return HttpResponse(f"Details for investigation {investigation_id}")
