from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "home/welcome.html", {"today": datetime.today()})


# Restricted to logged in users
@login_required(login_url="/admin")
def restricted(request):
    return render(request, "home/restricted.html", {})
