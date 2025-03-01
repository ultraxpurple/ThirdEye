# reports/views.py
from django.http import HttpResponse

def report_list(request):
    return HttpResponse("List of reports")

def view_report(request, report_id):
    return HttpResponse(f"Viewing report {report_id}")

def download_report(request, report_id):
    return HttpResponse(f"Downloading report {report_id}")

def rename_report(request, report_id):
    return HttpResponse(f"Renaming report {report_id}")

def delete_report(request, report_id):
    return HttpResponse(f"Deleting report {report_id}")
