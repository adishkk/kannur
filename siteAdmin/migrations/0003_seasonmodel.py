# Generated by Django 4.1.2 on 2022-11-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteAdmin', '0002_hobbymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
    ]
