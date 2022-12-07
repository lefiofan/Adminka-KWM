# Generated by Django 4.1.3 on 2022-11-08 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markirovka', '0005_alter_korob_aggr_alter_korob_nanes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страну'},
        ),
        migrations.AlterField(
            model_name='product',
            name='tara',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tara', to='markirovka.tara', verbose_name='Тара'),
        ),
    ]