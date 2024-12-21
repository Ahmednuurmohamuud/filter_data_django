# Generated by Django 5.1.3 on 2024-12-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgno', models.IntegerField()),
                ('pgname', models.CharField(max_length=30)),
                ('pgsal', models.FloatField()),
                ('pgaddr', models.CharField(max_length=30)),
            ],
        ),
    ]