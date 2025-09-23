from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data.get("first_name")
            last_name = data.get("last_name" )
            email = data.get("email")
            phone = data.get("phone")
            position = data.get("position")
            experience = data.get("experience")
            availability = data.get("availability")
            terms = data.get("terms")
            newsletter = data.get("newsletter")

            messages.success(request, "Application submitted successfully!")
            return redirect('index')  # Redirect to avoid form resubmission
        else:
            messages.error(request, "Please enter all the requirement")
            return redirect('index')
    else:
        form = ApplicationForm()  # Initialize form for GET request

    return render(request, "index.html" , {"form" : form})