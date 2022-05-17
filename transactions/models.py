from django.contrib.auth.models import User
from django.db import models

from settings.models import CategoryIncome, Tag, Account, CategoryExpenses


class Income(models.Model):
    name_income = models.CharField(max_length=100, help_text="Enter the name of the income", null=True, verbose_name="Name of income")
    summ_income = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")
    category_income = models.ForeignKey(CategoryIncome, on_delete=models.SET_NULL, null=True, verbose_name="Category")
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,verbose_name="User")
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tag")
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name="Account")
    note = models.TextField(verbose_name="Note", blank=True)

    STATUSES = [
        ("CNFD", "Confirmed"),
        ("NCNF", "Not confirmed"),
        ("WTNG", "Waiting")
    ]

    status = models.CharField(choices=STATUSES, max_length=4, default="CNFD", verbose_name="Status")
    img = models.ImageField(upload_to="images", blank=True, null=True, verbose_name="Image")
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Transaction date")

    class Meta:
        ordering = ["id"]
        verbose_name = "Income"

    def __str__(self):
        return self.name_income

class Expenses(models.Model):
    name_expenses = models.CharField(max_length=100, help_text="Enter the name of the expenses", unique=True, verbose_name="Name of expenses")
    summ_expenses = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")
    category_expenses = models.ForeignKey(CategoryExpenses, on_delete=models.SET_NULL, null=True, verbose_name="Category")
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name="User")
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tag")
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Account")
    note = models.TextField(verbose_name="Note", blank=True, null=True)

    STATUSES = [
        ("CNFD", "Confirmed"),
        ("NCNF", "Not confirmed"),
        ("WTNG", "Waiting")
    ]

    status = models.CharField(choices=STATUSES, max_length=4, default="CNFD", blank=True, null=True, verbose_name="Status")
    img = models.ImageField(upload_to="images", blank=True, null=True, verbose_name="Image")
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True,  verbose_name="Transaction date")

    class Meta:
        ordering = ["id"]
        verbose_name = "Expenses"

    def __str__(self):
        return self.name_expenses

class Transfer(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="from_account", null=True, verbose_name="From Account")
    to_account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="to_account", null=True, verbose_name="To Account")
    summ_transfer = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name="User")
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tag")
    note = models.TextField(verbose_name="Note", blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Transaction date")

    class Meta:
        ordering = ["id"]
        verbose_name = "Transfer"

    def __str__(self):
        return self.note