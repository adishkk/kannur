# Generated by Django 4.1.2 on 2022-11-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteAdmin', '0006_seasoncountrymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgefactorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Min_age', models.IntegerField()),
                ('Max_age', models.IntegerField()),
                ('Factor', models.CharField(max_length=255)),
            ],
        ),
    ]