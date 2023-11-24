# Generated by Django 4.1.2 on 2022-11-23 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_statemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('DOB', models.CharField(max_length=25)),
                ('Gender', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=50)),
                ('Security_question', models.CharField(max_length=500)),
                ('Answer', models.CharField(max_length=500)),
                ('Username', models.CharField(max_length=500)),
                ('Password', models.CharField(max_length=255)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.countrymodel')),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.statemodel')),
            ],
        ),
    ]