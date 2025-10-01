from django.shortcuts import render
from django.http import JsonResponse

def health(request):
    return JsonResponse({"ok": True, "feature": "budget_alerts"})

def alerts_page(request):
    return render(request, "budget_alerts/alerts.html")
# Create your views here.