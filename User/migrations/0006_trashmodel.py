# Generated by Django 4.1.2 on 2022-11-25 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_messagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrashModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=50)),
                ('Time', models.CharField(max_length=50)),
                ('Message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.messagemodel')),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.userregistrationmodel')),
            ],
        ),
    ]
