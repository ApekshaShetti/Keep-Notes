# Generated by Django 4.2.2 on 2023-08-10 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("QuickNotes", "0007_alter_note_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="password",),
    ]
