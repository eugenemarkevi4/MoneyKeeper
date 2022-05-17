from django.contrib import admin

from transactions.models import Income, Expenses, Transfer


class IncomeAdmin(admin.ModelAdmin):
    list_display = ("name_income", "summ_income", "category_income", "user", "tag", "account", "note", "status", "date")

admin.site.register(Income, IncomeAdmin)

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ("name_expenses", "summ_expenses", "category_expenses", "user", "tag", "account", "note", "status", "date")

admin.site.register(Expenses, ExpensesAdmin)

class TransferAdmin(admin.ModelAdmin):
    list_display = ("from_account", "to_account", "summ_transfer", "user", "tag", "note", "date")

admin.site.register(Transfer, TransferAdmin)