# Generated by Django 3.2.7 on 2022-04-28 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalityTest', '0017_auto_20220428_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='category',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='key',
        ),
    ]