# Generated by Django 2.1.3 on 2018-12-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_companycontact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='person',
            name='birthday',
        ),
    ]
