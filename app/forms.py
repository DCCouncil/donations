from django.forms import ModelForm
from app.models import Donation

class DonationForm(ModelForm):
    class Meta:
        model = Donation

from registration.forms import RegistrationForm
from django.forms import fields

class UserRegistrationForm(RegistrationForm):
    first_name = fields.CharField(max_length=200)
    last_name = fields.CharField(max_length=200)

    class Meta:
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')