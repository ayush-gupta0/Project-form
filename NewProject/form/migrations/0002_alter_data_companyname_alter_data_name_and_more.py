# Generated by Django 4.1.5 on 2023-01-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='CompanyName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='UserName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
