# Generated by Django 4.2.6 on 2023-11-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number',
            field=models.IntegerField(),
        ),
    ]
