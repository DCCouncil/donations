from django.shortcuts import render

#from app.forms import DonationForm
from app.models import Donation
from django.views.generic import ListView

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

class DonationListView(ListView):
    model = Donation