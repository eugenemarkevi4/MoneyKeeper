# Generated by Django 4.0.4 on 2022-05-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_income', models.CharField(help_text='Enter the name of the income', max_length=100, unique=True, verbose_name='Name of income')),
            ],
            options={
                'verbose_name': 'Income',
                'ordering': ['id'],
            },
        ),
    ]
