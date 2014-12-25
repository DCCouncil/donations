from django.forms import ModelForm
from app.models import Donation

class DonationForm(ModelForm):
	class Meta:
		model = Donation