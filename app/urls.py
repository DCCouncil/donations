from django.conf.urls import include, patterns, url
from . import views
from django.views.generic import ListView

urlpatterns = patterns('',
    url(r'', views.DonationListView.as_view()),
)