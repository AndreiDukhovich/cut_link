# Generated by Django 4.0.5 on 2022-07-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_users_link_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_link',
            name='cut_link',
            field=models.TextField(unique=True, verbose_name='Cut link'),
        ),
        migrations.AlterField(
            model_name='users_link',
            name='long_link',
            field=models.TextField(unique=True, verbose_name='Long link'),
        ),
    ]
