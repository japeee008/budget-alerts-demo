from django.shortcuts import render
from django.http import JsonResponse

def health(request):
    return JsonResponse({"ok": True, "feature": "budget_alerts"})
# Create your views here.
