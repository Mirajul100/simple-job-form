from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from .forms import ApplicationForm
from .models import Form

def index(request):
    try :
        if request.method == "POST":
            form = ApplicationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                first_name = data.get("first_name")
                last_name = data.get("last_name" )
                email = data.get("email")
                phone = data.get("phone")
                position = data.get("position")
                experience = data.get("experience" , "")
                availability = data.get("availability" , None)
                terms = data.get("terms")
                newsletter = data.get("newsletter")

                Form.objects.create(first_name= first_name,
                                    last_name= last_name,
                                    email= email,
                                    phone= phone,
                                    position= position,
                                    experience= experience,
                                    availability= availability,
                                    terms = terms,
                                    newsletter = newsletter)

                messages.success(request, "Application submitted successfully!")
                return redirect('index')  # Redirect to avoid form resubmission
            else:
                messages.error(request, "Please enter all the requirement")
                return redirect('index')
        else:
            form = ApplicationForm()  # Initialize form for GET request
    except IntegrityError:
        messages.error(request, "You have already submitted this form.")
        return redirect('index')

    return render(request, "index.html", {"form": form})
