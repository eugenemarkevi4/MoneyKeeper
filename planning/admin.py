from django.contrib import admin

from planning.models import Budget, PlanningIncome, PlanningExpenses

class BudgetAdmin(admin.ModelAdmin):
    list_display = ("category", "summ_expenses", "date")

admin.site.register(Budget, BudgetAdmin)

class PlanningIncomeAdmin(admin.ModelAdmin):
    list_display = ("income", "category", "summ_income", "note", "date")

admin.site.register(PlanningIncome, PlanningIncomeAdmin)

class PlanningExpensesAdmin(admin.ModelAdmin):
    list_display = ("expenses", "category", "summ_expenses", "note", "date")

admin.site.register(PlanningExpenses, PlanningExpensesAdmin)
