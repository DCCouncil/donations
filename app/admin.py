from django.contrib import admin
from app.models import Donation

# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

make_published.short_description = "Mark selected stories as published"

class DonationAdmin(admin.ModelAdmin):
    list_display = ('description', 'donor', 'donation_date','amount','status')
    search_fields = ('description', 'donor')
    ordering = ('-donation_date',)
    fields = ('description', 'donor', 'donation_date', 'amount', 'notes', 'status')
    actions = ['make_published']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(DonationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
            # Now we just add an extra filter on the queryset and
            # we're done. Assumption: Page.owner is a foreignkey
            # to a User.
        return qs.filter(created_by=request.user)

admin.site.register(Donation, DonationAdmin)