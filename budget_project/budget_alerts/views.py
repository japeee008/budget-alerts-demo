from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import BudgetAlertForm
from .models import BudgetAlert, Category

def alerts_page(request):
    print(f"User: {request.user}")  # Debugging: print the current logged-in user

    if request.user.is_authenticated:
        # Fetch categories only for the logged-in user
        categories = Category.objects.filter(user=request.user).order_by("name")
        print(f"Categories fetched: {categories}")  # Debugging line to check categories

        if not categories.exists():
            print("No categories found. Creating default categories.")  # Debugging line
            # Seed categories if none exist for the logged-in user
            for n in ["Food", "Transport", "Leisure", "Bills", "School Supplies"]:
                Category.objects.get_or_create(user=request.user, name=n)
            categories = Category.objects.filter(user=request.user)
            print(f"Categories after creation: {categories}")  # Debugging line
    else:
        # If user isn't logged in, fetch all categories (for testing purposes)
        categories = Category.objects.all()
        print("User is not authenticated. Proceeding without user-specific categories.")  # Debugging line

    # Handle form submission
    if request.method == "POST":
        form = BudgetAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            if request.user.is_authenticated:
                alert.user = request.user  # Set the user to the logged-in user
            alert.save()  # Save the alert to the database
            print(f"Saved alert: {alert}")  # Debugging line to confirm alert is saved
            messages.success(request, "Budget alert saved successfully.")
            return redirect("alerts_page")  # Redirect to avoid resubmission
    else:
        form = BudgetAlertForm()

    # Fetch only active alerts for the logged-in user
    alerts = BudgetAlert.objects.filter(user=request.user, active=True) if request.user.is_authenticated else []
    return render(request, "alerts.html", {
        "form": form,
        "alerts": alerts,  # Pass the active alerts to the template
        "categories": categories  # Pass categories to the template for the dropdown
    })
