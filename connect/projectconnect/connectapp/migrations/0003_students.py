# Generated by Django 5.1.3 on 2024-12-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectapp', '0002_programmer_pgemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('ssal', models.FloatField()),
                ('saddr', models.CharField(max_length=30)),
            ],
        ),
    ]