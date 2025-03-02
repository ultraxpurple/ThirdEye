# investigations/views.py
from django.http import HttpResponse
from .models import Investigation

def investigation_list(request):
    # Fetch investigations (which include report information)
    investigations = Investigation.objects.filter(user=request.user)
    return render(request, 'investigations/investigation_list.html', {'investigations': investigations})
