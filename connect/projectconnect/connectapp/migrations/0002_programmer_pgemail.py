# Generated by Django 5.1.3 on 2024-12-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmer',
            name='pgemail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
