from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from tastypie.api import Api
from app.api.resources import DonationResource

v1_api = Api(api_name='v1')
v1_api.register(DonationResource())

from app.views import Register
from app.forms import UserRegistrationForm
from registration.backends.default.views import RegistrationView, ActivationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^about/$', 'app.views.about', name='about'),
    url(r'accounts/register/$', RegistrationView.as_view(form_class = UserRegistrationForm), name = 'registration_register'), 
	url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(get_success_url='/admin'), name="registration_activate"),
    url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^donations/', include('app.urls', namespace="app")),
    url(r'^api/', include(v1_api.urls)),
)