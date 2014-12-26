from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from tastypie.api import Api
from app.api.resources import DonationResource

v1_api = Api(api_name='v1')
v1_api.register(DonationResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^donations/', include('app.urls', namespace="app")),
    url(r'^api/', include(v1_api.urls)),
)