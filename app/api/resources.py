from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from app.models import Donation
from tastypie.authorization import ReadOnlyAuthorization


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ['username','email', 'password', 'is_active', 'is_staff', 'is_superuser','id','last_login','date_joined']

class DonationResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'created_by', full=True)

    class Meta:
        queryset = Donation.objects.all()
        allowed_methods = ['get']
        authorization = ReadOnlyAuthorization()
        resources = "donations"