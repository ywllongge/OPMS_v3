# Generated by Django 2.0.6 on 2018-07-09 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host_management', '0002_operatingsysteminfo_bit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectinfo',
            options={'verbose_name': '项目', 'verbose_name_plural': '项目'},
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='op_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_op_user', to=settings.AUTH_USER_MODEL, verbose_name='运维人员'),
        ),
    ]
