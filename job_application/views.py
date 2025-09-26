from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from .forms import ApplicationForm
from .models import Form
from django.core.mail import EmailMessage
from .admin import AdminForm

def index(request):
    try :
        if request.method == "POST":
            form = ApplicationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                first_name = data.get("first_name").title()
                last_name = data.get("last_name" ).title()
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
                
                email_body = f"New Job Form submitted \nThank you {first_name} {last_name}"
                email_message = EmailMessage("Form submission conformation" , email_body , to=[email])
                email_message.send()

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

def about(request):
    return render(request , "about.html")

def contact(request):
    return render(request , "contact.html")

def admin(request):
    admin = AdminForm()
    return render(request , "admin")