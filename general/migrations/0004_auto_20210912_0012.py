# Generated by Django 3.1.2 on 2021-09-11 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20210911_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',)},
        ),
    ]