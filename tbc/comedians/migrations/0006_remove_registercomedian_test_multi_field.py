# Generated by Django 2.2.1 on 2019-10-27 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comedians', '0005_registercomedian_test_multi_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registercomedian',
            name='test_multi_field',
        ),
    ]
