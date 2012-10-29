from partners.models import Partner

from django.contrib import admin


class PartnerAdmin(admin.ModelAdmin):
    pass

print "yo is this module real"

admin.site.register(Partner, PartnerAdmin)
