from PIL import Image
from django.db import models
from django_resized import ResizedImageField

from transliterate import translit

def upload_to(instance, filename):

    filebase, extension = filename.split('.')
    if extension == 'apng':
        extension = 'png'
    en_nameImages = translit(instance.title, language_code='ru', reversed=True)
    return 'images/%s.%s' % (en_nameImages, extension)
class Country(models.Model):
    name = models.CharField(name="name", max_length=100, unique=True, verbose_name="Страна")

    class Meta:
        verbose_name = u"Страна"
        verbose_name_plural = u"Страну"

    def __str__(self):
        return self.name
class Tara(models.Model):
    name = models.CharField(name="name", max_length=100, unique=True, verbose_name="Тара")

    class Meta:
        verbose_name = u"Тара"
        verbose_name_plural = u"Тары"

    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(name='title', max_length=100, verbose_name="Название")
    img = ResizedImageField(size=[500, 500], quality=75, upload_to=upload_to, blank=True, null=True, verbose_name="Картинка")
    gtin = models.CharField(name='gtin', max_length=28, verbose_name="GTIN")
    created = models.DateField(auto_now_add=True, db_index=True, verbose_name="Создание")
    tara = models.ForeignKey(Tara, on_delete=models.CASCADE, related_name='tara',  verbose_name="Тара")

    class Meta:
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукты"

    def __str__(self):
        return self.title
class Donwload_codes(models.Model):
    code = models.CharField(name='code', max_length=100, verbose_name="Тара")
    aggr = models.BooleanField(default=False, null=True, verbose_name="Агригирован")
    nanes = models.BooleanField(default=False, null=True, verbose_name="Нанесенн")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукты")


    class Meta:
        verbose_name = u"Потребительский код"
        verbose_name_plural = u"Потребительские коды"

    def __str__(self):
        return self.code
class Donwload_codes_korob(models.Model):
    code = models.CharField(name='code', max_length=100, verbose_name="Код")
    aggr = models.BooleanField(default=False, null=True, verbose_name="Агригирован")
    nanes = models.BooleanField(default=False, null=True, verbose_name="Нанесенн")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна")
    class Meta:
        verbose_name = u"Групповой код"
        verbose_name_plural = u"Групповое коды"

    def __str__(self):
        return self.code
class Korob(models.Model):
    products_code = models.TextField(name='products_code', max_length=1000, default='0', verbose_name="Потребительские коды")
    korob_code = models.ForeignKey(Donwload_codes_korob, on_delete=models.CASCADE, verbose_name="Групповой код")
    status = models.BooleanField(default=False, null=True, verbose_name="Статус")
    aggr = models.BooleanField(default=False, null=True, verbose_name="Агригирован")
    nanes = models.BooleanField(default=False, null=True, verbose_name="Нанесенн")

    class Meta:
        verbose_name = u"Ящик"
        verbose_name_plural = u"Ящики"
        ordering = ['korob_code']
    def __str__(self):
        return self.korob_code