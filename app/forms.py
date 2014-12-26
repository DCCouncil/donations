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

#     def __init__(self, *args, **kw):
#        super(SignupForm, self).__init__(*args, **kw)

#     def save(self):
#         #first save the parent form
#         profile = super(SignupForm, self).save()
#         #then save the custom fields
#         #i am assuming that the parent form return a profile
#         profile.last_name = self.cleaned_data['last_name']
#         profile.country = self.cleaned_data['first_name']
#         profile.save()
#         return profile

    class Meta:
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')