from django.db import models

class CategoryIncome(models.Model):
    category = models.CharField(max_length=100, help_text="Enter the name of the Category", null=True, verbose_name="Name of Category")

    class Meta:
        ordering = ["id"]
        verbose_name = "Category Income"

    def __str__(self):
        return self.category

class CategoryExpenses(models.Model):
    category = models.CharField(max_length=100, help_text="Enter the name of the Category", null=True, verbose_name="Name of Category")

    class Meta:
        ordering = ["id"]
        verbose_name = "Category Expenses"

    def __str__(self):
        return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=100, help_text="Enter the name of the Tag", null=True, verbose_name="Name of Tag")

    class Meta:
        ordering = ["id"]
        verbose_name = "Tag"

    def __str__(self):
        return self.tag

class Account(models.Model):
    account = models.CharField(max_length=100, help_text="Enter the name of the Account", null=True, verbose_name="Name of Account")
    ACCOUNT = [
        ("CSH", "Cash"),
        ("DBT", "Debit"),
        ("CRD", "Credit"),
        ("SAC", "Savings Account")
    ]

    account_type = models.CharField(choices=ACCOUNT, max_length=4, blank=True, verbose_name="Account Type")

    class Meta:
        ordering = ["id"]
        verbose_name = "Account"

    def __str__(self):
        return self.account