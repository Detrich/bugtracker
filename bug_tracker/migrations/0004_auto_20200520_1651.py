# Generated by Django 3.0.6 on 2020-05-20 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug_tracker', '0003_auto_20200520_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='usercompleted',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='usercompleted', to=settings.AUTH_USER_MODEL),
        ),
    ]