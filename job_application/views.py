from django.shortcuts import render
from .forms import ApplicationForm

def index(request):

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name   = data.get("firstName", "")
            last_name    = data.get("lastName", "")
            email        = data.get("email", "")
            phone        = data.get("phone", "")
            position     = data.get("position", "")
            experience   = data.get("experience", "")
            availability = data.get("availability", None)
            terms        = data.get("terms", False)
            newsletter   = data.get("newsletter", False)

            print (first_name)
    
    return render(request , "index.html")