from django.db import models

from settings.models import CategoryExpenses, CategoryIncome


class Budget(models.Model):
    category = models.ForeignKey(CategoryExpenses, on_delete=models.SET_NULL, null=True, verbose_name="Category")
    summ_expenses = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")
    date = models.DateField(null=True, blank=True, verbose_name="Budget date")

    class Meta:
        ordering = ["id"]
        verbose_name = "Budget"

    def __str__(self):
        return str(self.category)

class PlanningIncome(models.Model):
    income = models.CharField(max_length=100, help_text="Enter the name of the Income", unique=True, verbose_name="Name of Income")
    category = models.ForeignKey(CategoryIncome, on_delete=models.SET_NULL, null=True, verbose_name="Category")
    summ_income = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")
    note = models.TextField(verbose_name="Note", blank=True)
    date = models.DateField(auto_now_add=True, null=True, verbose_name="Date Income")

    class Meta:
        ordering = ["id"]
        verbose_name = "Planning Income"

    def __str__(self):
        return self.income

class PlanningExpenses(models.Model):
    expenses = models.CharField(max_length=100, help_text="Enter the name of the Expenses", unique=True, verbose_name="Name of Expenses")
    category = models.ForeignKey(CategoryExpenses, on_delete=models.SET_NULL, null=True, verbose_name="Category")
    summ_expenses = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")
    note = models.TextField(verbose_name="Note", blank=True)
    date = models.DateField(auto_now_add=True, null=True, verbose_name="Date Expenses")

    class Meta:
        ordering = ["id"]
        verbose_name = "Planning Expenses"

    def __str__(self):
        return self.expenses