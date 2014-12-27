from django.shortcuts import render

#from app.forms import DonationForm
from app.models import Donation
from django.views.generic import ListView

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

class DonationListView(ListView):
    model = Donation

from registration.views import RegistrationView
# from django.contrib.auth.models import User
from app.forms import UserRegistrationForm

class Register(RegistrationView):
    form_class = UserRegistrationForm


from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from registration.signals import user_registered
def user_created(sender, user, request, **kwargs):
    """
    Called via signals when user registers. Creates different profiles and
    associations
    """
    form = UserRegistrationForm(request.POST)
    # Update first and last name for user
    user.first_name=form.data['first_name']
    user.last_name=form.data['last_name']
    user.is_staff = True

    content_type = ContentType.objects.get_for_model(Donation)
    permission_add = Permission.objects.get(content_type=content_type, codename='add_donation')
    permission_change = Permission.objects.get(content_type=content_type, codename='change_donation')
    permission_delete = Permission.objects.get(content_type=content_type, codename='delete_donation')
    user.user_permissions.add(permission_add,permission_change,permission_delete)
    user.save()
 
user_registered.connect(user_created)
