# Generated by Django 3.0.6 on 2020-05-20 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug_tracker', '0006_auto_20200520_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='usersubmited',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='usersubmitted', to=settings.AUTH_USER_MODEL),
        ),
    ]