# Generated by Django 4.2.6 on 2023-11-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='blog.tag'),
        ),
    ]
