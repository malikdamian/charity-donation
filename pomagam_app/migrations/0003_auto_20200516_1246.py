# Generated by Django 3.0.6 on 2020-05-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomagam_app', '0002_auto_20200516_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
