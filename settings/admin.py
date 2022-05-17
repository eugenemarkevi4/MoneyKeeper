from django.contrib import admin

from settings.models import CategoryIncome, CategoryExpenses, Tag, Account

admin.site.register(CategoryIncome)
admin.site.register(CategoryExpenses)
admin.site.register(Tag)
admin.site.register(Account)