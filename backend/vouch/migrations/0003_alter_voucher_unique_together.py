# Generated by Django 4.0.7 on 2022-08-14 13:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("vouch", "0002_trust_value_isnow_value"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="voucher",
            unique_together={("by", "to")},
        ),
    ]