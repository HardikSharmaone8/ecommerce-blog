# Generated by Django 4.0.6 on 2022-08-13 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='pub_date',
        ),
    ]
