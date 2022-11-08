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
    name = models.CharField(name="name", max_length=100, unique=True)

    class Meta:
        verbose_name = u"Страна"
        verbose_name_plural = u"Страны"

    def __str__(self):
        return self.name

class Tara(models.Model):
    name = models.CharField(name="name", max_length=100, unique=True)

    class Meta:
        verbose_name = u"Тара"
        verbose_name_plural = u"Тары"

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(name='title', max_length=100)
    img = ResizedImageField(size=[500, 500], quality=75, upload_to=upload_to, blank=True, null=True)
    gtin = models.CharField(name='gtin', max_length=28)
    created = models.DateField(auto_now_add=True, db_index=True)
    tara = models.ForeignKey(Tara, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукты"

    def __str__(self):
        return self.title






class Donwload_codes(models.Model):
    code = models.CharField(name='code', max_length=100)
    aggr = models.BooleanField(default=False, null=True)
    nanes = models.BooleanField(default=False, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        verbose_name = u"Код потребительский"
        verbose_name_plural = u"Коды потребительские"

    def __str__(self):
        return self.code

class Donwload_codes_korob(models.Model):
    code = models.CharField(name='code', max_length=100)
    aggr = models.BooleanField(default=False, null=True)
    nanes = models.BooleanField(default=False, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    class Meta:
        verbose_name = u"Код коробки"
        verbose_name_plural = u"Коды коробкок"

    def __str__(self):
        return self.code

class Korob(models.Model):
    products_code = models.TextField(name='products_code', max_length=1000, default='0')
    korob_code = models.CharField(name='korob_code', max_length=1000)
    korob_code = models.ForeignKey(Donwload_codes_korob, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, null=True)
    aggr = models.CharField(name='aggr', max_length=1000, null=True, default='0')
    nanes = models.CharField(name='nanes', max_length=1000, null=True, default='0')

    class Meta:
        verbose_name = u"Ящик"
        verbose_name_plural = u"Ящики"
        ordering = ['korob_code']
    def __str__(self):
        return self.korob_code