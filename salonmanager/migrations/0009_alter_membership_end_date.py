# Generated by Django 4.2.2 on 2023-07-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salonmanager', '0008_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
