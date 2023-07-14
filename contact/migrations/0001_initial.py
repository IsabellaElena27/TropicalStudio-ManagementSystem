# Generated by Django 4.2.1 on 2023-07-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=40)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]
