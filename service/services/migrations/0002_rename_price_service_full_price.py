# Generated by Django 3.2.16 on 2023-10-17 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='price',
            new_name='full_price',
        ),
    ]