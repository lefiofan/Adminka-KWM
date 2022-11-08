# Generated by Django 4.1.3 on 2022-11-08 16:19

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import markirovka.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Donwload_codes_korob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('aggr', models.BooleanField(default=False, null=True)),
                ('nanes', models.BooleanField(default=False, null=True)),
                ('country.py', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.country.py')),
            ],
            options={
                'verbose_name': 'Код коробки',
                'verbose_name_plural': 'Коды коробкок',
            },
        ),
        migrations.CreateModel(
            name='Tara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Тара',
                'verbose_name_plural': 'Тары',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, scale=None, size=[500, 500], upload_to=markirovka.models.upload_to)),
                ('gtin', models.CharField(max_length=28)),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('tara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.tara')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Korob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_code', models.TextField(default='0', max_length=1000)),
                ('status', models.BooleanField(default=False, null=True)),
                ('aggr', models.CharField(default='0', max_length=1000, null=True)),
                ('nanes', models.CharField(default='0', max_length=1000, null=True)),
                ('korob_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.donwload_codes_korob')),
            ],
            options={
                'verbose_name': 'Ящик',
                'verbose_name_plural': 'Ящики',
                'ordering': ['korob_code'],
            },
        ),
        migrations.CreateModel(
            name='Donwload_codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('aggr', models.BooleanField(default=False, null=True)),
                ('nanes', models.BooleanField(default=False, null=True)),
                ('country.py', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.country.py')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markirovka.product')),
            ],
            options={
                'verbose_name': 'Код потребительский',
                'verbose_name_plural': 'Коды потребительские',
            },
        ),
    ]
