# Generated by Django 3.1.2 on 2021-09-20 02:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0024_auto_20210920_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='killnumber',
            name='blueBall',
            field=models.CharField(default=[], max_length=1024, validators=[django.core.validators.int_list_validator], verbose_name='蓝球'),
        ),
    ]