# Generated by Django 4.1 on 2022-08-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Product_Id',
            field=models.CharField(max_length=1000),
        ),
    ]
