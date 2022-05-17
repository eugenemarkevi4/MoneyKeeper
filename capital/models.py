from django.db import models

from settings.models import Account


class Capital(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name="Account")
    summ_сapital = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")

    class Meta:
        ordering = ["id"]
        verbose_name = "Capital"

    def __str__(self):
        return str(self.account)

class Assets(models.Model):
    name_assets = models.CharField(max_length=100, help_text="Enter the name of the Assets", unique=True, verbose_name="Name of Assets")
    summ_assets = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")

    class Meta:
        ordering = ["id"]
        verbose_name = "Assets"

    def __str__(self):
        return self.name_assets

class Liabilities(models.Model):
    name_liabilities = models.CharField(max_length=100, help_text="Enter the name of the Liabilities", unique=True, verbose_name="Name of Liabilities")
    summ_liabilities = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the amount in $", null=True, verbose_name="Amount in $")
    interest_rate = models.DecimalField(max_digits=20, decimal_places=2, help_text="Enter the interest rate in %", null=True, verbose_name="Interest rate in %")

    class Meta:
        ordering = ["id"]
        verbose_name = "Liabilities"

    def __str__(self):
        return self.name_liabilities