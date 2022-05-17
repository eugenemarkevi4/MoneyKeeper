# Generated by Django 4.0.4 on 2022-05-05 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0005_account_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_assets', models.CharField(help_text='Enter the name of the Assets', max_length=100, unique=True, verbose_name='Name of Assets')),
                ('summ_assets', models.DecimalField(decimal_places=2, help_text='Enter the amount in $', max_digits=20, null=True, verbose_name='Amount in $')),
            ],
            options={
                'verbose_name': 'Assets',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Liabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_liabilities', models.CharField(help_text='Enter the name of the Liabilities', max_length=100, unique=True, verbose_name='Name of Liabilities')),
                ('summ_liabilities', models.DecimalField(decimal_places=2, help_text='Enter the amount in $', max_digits=20, null=True, verbose_name='Amount in $')),
                ('interest_rate', models.DecimalField(decimal_places=2, help_text='Enter the interest rate in %', max_digits=20, null=True, verbose_name='Interest rate in %')),
            ],
            options={
                'verbose_name': 'Liabilities',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summ_сapital', models.DecimalField(decimal_places=2, help_text='Enter the amount in $', max_digits=20, null=True, verbose_name='Amount in $')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.account', verbose_name='Account')),
            ],
            options={
                'verbose_name': 'Capital',
                'ordering': ['id'],
            },
        ),
    ]