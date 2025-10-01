from django.http import JsonResponse
from django.shortcuts import render

def health(request):
    return JsonResponse({"ok": True, "feature": "budget_alerts"})

def alerts_page(request):
    return render(request, "alerts.html")
# Create your views here.