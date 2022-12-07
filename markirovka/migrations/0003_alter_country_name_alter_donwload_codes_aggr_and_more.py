# Generated by Django 4.1.3 on 2022-11-08 17:17

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import markirovka.models


class Migration(migrations.Migration):

    dependencies = [
        ('markirovka', '0002_alter_tara_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='donwload_codes',
            name='aggr',
            field=models.BooleanField(default=False, null=True, verbose_name='Агригирован'),
        ),
        migrations.AlterField(
            model_name='donwload_codes',
            name='code',
            field=models.CharField(max_length=100, verbose_name='Тара'),
        ),
        migrations.AlterField(
            model_name='donwload_codes',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='donwload_codes',
            name='nanes',
            field=models.BooleanField(default=False, null=True, verbose_name='Нанесенн'),
        ),
        migrations.AlterField(
            model_name='donwload_codes',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.product', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='donwload_codes_korob',
            name='aggr',
            field=models.BooleanField(default=False, null=True, verbose_name='Агригирован'),
        ),
        migrations.AlterField(
            model_name='donwload_codes_korob',
            name='code',
            field=models.CharField(max_length=100, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='donwload_codes_korob',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='donwload_codes_korob',
            name='nanes',
            field=models.BooleanField(default=False, null=True, verbose_name='Нанесенн'),
        ),
        migrations.AlterField(
            model_name='korob',
            name='aggr',
            field=models.CharField(default='0', max_length=1000, null=True, verbose_name='Агригирован'),
        ),
        migrations.AlterField(
            model_name='korob',
            name='korob_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.donwload_codes_korob', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='korob',
            name='nanes',
            field=models.CharField(default='0', max_length=1000, null=True, verbose_name='Нанесенн'),
        ),
        migrations.AlterField(
            model_name='korob',
            name='products_code',
            field=models.TextField(default='0', max_length=1000, verbose_name='Потребительские коды'),
        ),
        migrations.AlterField(
            model_name='korob',
            name='status',
            field=models.BooleanField(default=False, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Создание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gtin',
            field=models.CharField(max_length=28, verbose_name='GTIN'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, scale=None, size=[500, 500], upload_to=markirovka.models.upload_to, verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.tara', verbose_name='Тара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]