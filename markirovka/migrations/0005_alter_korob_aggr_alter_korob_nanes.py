# Generated by Django 4.1.3 on 2022-11-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markirovka', '0004_alter_donwload_codes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korob',
            name='aggr',
            field=models.BooleanField(default=False, null=True, verbose_name='Агригирован'),
        ),
        migrations.AlterField(
            model_name='korob',
            name='nanes',
            field=models.BooleanField(default=False, null=True, verbose_name='Нанесенн'),
        ),
    ]
