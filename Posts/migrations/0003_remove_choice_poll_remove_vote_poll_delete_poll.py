# Generated by Django 4.2.3 on 2023-08-17 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]