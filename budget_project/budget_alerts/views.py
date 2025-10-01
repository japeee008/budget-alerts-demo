from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BudgetAlertForm
from .models import BudgetAlert, Category

def health(request):
    return JsonResponse({"ok": True, "feature": "budget_alerts"})

@login_required
def alerts_page(request):
    # minimal: show only current user's data
    categories = Category.objects.filter(user=request.user).order_by("name")
    if not categories.exists():
        # seed a few categories for testing
        for n in ["Food","Transport","Leisure","Bills","School Supplies"]:
            Category.objects.get_or_create(user=request.user, name=n)
        categories = Category.objects.filter(user=request.user)

    if request.method == "POST":
        form = BudgetAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            messages.success(request, "Budget alert saved successfully.")
            return redirect("alerts_page")
    else:
        form = BudgetAlertForm()

    alerts = BudgetAlert.objects.filter(user=request.user)
    return render(request, "alerts.html", {"form": form, "alerts": alerts, "categories": categories})

# Create your views here.