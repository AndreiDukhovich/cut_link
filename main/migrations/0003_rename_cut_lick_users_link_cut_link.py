# Generated by Django 4.0.5 on 2022-07-08 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_users_link_delete_users_links'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_link',
            old_name='cut_lick',
            new_name='cut_link',
        ),
    ]