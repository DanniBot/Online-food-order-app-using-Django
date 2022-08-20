# Generated by Django 3.2.5 on 2022-08-20 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_openinghour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghour',
            options={'ordering': ('day', '-from_hour')},
        ),
        migrations.AlterUniqueTogether(
            name='openinghour',
            unique_together={('vendor', 'day', 'from_hour', 'to_hour')},
        ),
    ]
