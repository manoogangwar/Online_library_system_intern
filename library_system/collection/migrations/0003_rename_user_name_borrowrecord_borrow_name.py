# Generated by Django 5.2 on 2025-04-12 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_alter_author_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowrecord',
            old_name='user_name',
            new_name='borrow_name',
        ),
    ]
