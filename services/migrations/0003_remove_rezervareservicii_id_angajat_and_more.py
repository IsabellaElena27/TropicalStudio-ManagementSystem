# Generated by Django 4.2.1 on 2023-07-13 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rezervareservicii_programare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rezervareservicii',
            name='id_angajat',
        ),
        migrations.DeleteModel(
            name='Programare',
        ),
    ]
