# Generated by Django 3.2.2 on 2021-05-07 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='user_id',
        ),
    ]
