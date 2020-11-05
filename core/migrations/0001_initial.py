# Generated by Django 3.1.3 on 2020-11-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20, unique=True)),
                ('password', models.TextField(max_length=200)),
                ('full_name', models.TextField(max_length=100)),
                ('email_address', models.TextField(max_length=100, unique=True)),
                ('phone_number', models.TextField(max_length=20, unique=True)),
                ('current_address', models.TextField(max_length=200)),
                ('account_status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
            ],
        ),
    ]
