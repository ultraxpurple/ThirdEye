# contact/views.py
from django.http import HttpResponse

def contact_form(request):
    return HttpResponse("Contact form page")

def submit_contact(request):
    return HttpResponse("Contact form submitted")
