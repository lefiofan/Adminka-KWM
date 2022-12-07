from django import forms

from markirovka.models import Country, Product


class UploadItemCsvFileForm(forms.Form):
    country = forms.ModelChoiceField(empty_label='Выберите Страну', label='Страна', queryset=Country.objects.all())
    products = forms.ModelChoiceField(empty_label='Выберите Продукт', label='Продукт',queryset=Product.objects.all())
    file = forms.FileField(label='Выберите файл с кодами')

