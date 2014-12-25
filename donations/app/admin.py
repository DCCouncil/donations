from django.contrib import admin
from app.models import Donation

# Register your models here.

class DonationAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"created_by": ("created_by",)}
    list_display = ('description', 'donor', 'donation_date','amount')
    search_fields = ('description', 'donor')
    ordering = ('-donation_date',)
    fields = ('description', 'donor', 'donation_date', 'amount', 'notes', )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()

    def queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(DonationAdmin, self).queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
            # Now we just add an extra filter on the queryset and
            # we're done. Assumption: Page.owner is a foreignkey
            # to a User.
        return qs.filter(created_by=request.user)

admin.site.register(Donation, DonationAdmin)