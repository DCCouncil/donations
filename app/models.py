from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donation(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True)
    donation_date = models.DateField('Donation Date', blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=200, blank=True, null=True)
    donor = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)

    def __unicode__(self):
        return "[%s, %s, %s]" % (self.donor, self.donation_date, self.description)