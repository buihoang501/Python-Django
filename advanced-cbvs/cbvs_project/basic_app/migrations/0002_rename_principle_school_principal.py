# Generated by Django 4.1 on 2023-10-18 10:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("basic_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="school",
            old_name="principle",
            new_name="principal",
        ),
    ]