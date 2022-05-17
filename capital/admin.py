from django.contrib import admin

from capital.models import Capital, Assets, Liabilities


class CapitalAdmin(admin.ModelAdmin):
    list_display = ("account", "summ_сapital")

admin.site.register(Capital, CapitalAdmin)

class AssetsAdmin(admin.ModelAdmin):
    list_display = ("name_assets", "summ_assets")

admin.site.register(Assets, AssetsAdmin)

class LiabilitiesAdmin(admin.ModelAdmin):
    list_display = ("name_liabilities", "summ_liabilities", "interest_rate")

admin.site.register(Liabilities, LiabilitiesAdmin)