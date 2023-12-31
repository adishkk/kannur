# Generated by Django 4.1.2 on 2022-11-23 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteAdmin', '0002_hobbymodel'),
        ('User', '0003_userregistrationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHobbyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hobbies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteAdmin.hobbymodel')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.userregistrationmodel')),
            ],
        ),
    ]
