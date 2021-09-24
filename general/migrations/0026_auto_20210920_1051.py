# Generated by Django 3.1.2 on 2021-09-20 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0025_auto_20210920_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='killnumber',
            name='blueBall',
            field=models.CharField(default=[], max_length=100, validators=[django.core.validators.int_list_validator], verbose_name='蓝球'),
        ),
        migrations.AlterField(
            model_name='killnumber',
            name='redBall',
            field=models.CharField(default=[], max_length=256, validators=[django.core.validators.int_list_validator], verbose_name='红球'),
        ),
    ]