import csv

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.safestring import mark_safe
from import_export.fields import Field
from import_export.forms import ImportForm, ConfirmImportForm

from .forms import UploadItemCsvFileForm
from .models import Product, Korob, Donwload_codes, Donwload_codes_korob, Country, Tara, Download_codes_files
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    #search_fields = ("title", "gtin")
    list_display = ('name',)

@admin.register(Tara)
class TaraAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("title", "gtin")
    list_display = ('title',  'gtin', 'tara')
    readonly_fields = ('get_img',)


    fieldsets = (
        (None, {
            'fields': ("title", "gtin", "tara")
        }),
        (None, {
            'fields': ("img", "get_img")
        }),

    )
    def get_img(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="250" height="250">')
    get_img.short_description = "Изображение"

@admin.register(Donwload_codes)
class Donwload_codesAdmin(admin.ModelAdmin):

   list_filter = ('aggr', 'nanes', 'products',)
   search_fields = ("code",)
   list_display = ('code', 'aggr', 'nanes', 'country', 'products')

   change_list_template = "admin/change_list_codes_.html"


   def create_task_view(self, request, queryset):
       if request.method == 'POST':
           form = UploadItemCsvFileForm(request.POST, request.FILES)
           if form.is_valid():
               country = Country.objects.filter(id=request.POST['country']).get()
               product = Product.objects.filter(id=request.POST['products']).get()

               newdoc = Download_codes_files(name=request.FILES['file'])
               newdoc.save()


               urk = Download_codes_files.objects.get(id=newdoc.id)

               with open(f'media/{urk.name}') as csv_file:
                   csv_reader = csv.reader(csv_file, delimiter=' ')
                   for code in csv_reader:
                       # Проверить GTIN доп проверка
                       cod = code[0].split(' ')
                       new_codes = Donwload_codes(code=cod, country=country, products=product)
                       new_codes.save()
               return HttpResponseRedirect('my-view')
           else:
               form = UploadItemCsvFileForm(request.POST, request.FILES)

               return render(request, 'create_task.html', {
                   'title': 'Create task for selected items',
                   'itmes': queryset,
                   'form': form
               })



@admin.register(Donwload_codes_korob)
class Donwload_codes_korobAdmin(admin.ModelAdmin):
    list_filter = ( 'aggr', 'nanes',)
    search_fields = ("code",)
    list_display = ('code', 'aggr', 'nanes',)

@admin.register(Korob)
class KorobAdmin(admin.ModelAdmin):
    list_display = ('korob_code', 'status', 'aggr', 'nanes',)
    list_filter = ('status', 'aggr', 'nanes',)
    filter_horizontal = ['products_code']

admin.site.site_title = "Минвода Маркировка"
admin.site.site_header = "Маркировка"