from django.contrib import admin
from .models import Product, Korob, Donwload_codes, Donwload_codes_korob, Country, Tara
from import_export import resources
from import_export.admin import ImportExportModelAdmin


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
    list_display = ('title', 'img', 'gtin', 'tara')

#
# class Donwload_codesAdmin(admin.ModelAdmin):

class StudentResource(resources.ModelResource):
   class Meta:
      model = Donwload_codes
      fields = ('code',)

@admin.register(Donwload_codes)
class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource
   list_filter = ('aggr', 'nanes',)
   search_fields = ("code",)
   list_display = ('code', 'aggr', 'nanes', 'country', 'products')

   change_list_template = "admin/change_list_codes_.html"
@admin.register(Donwload_codes_korob)
class Donwload_codes_korobAdmin(admin.ModelAdmin):
    list_filter = ( 'aggr', 'nanes',)
    search_fields = ("code",)
    list_display = ('code', 'aggr', 'nanes',)

@admin.register(Korob)
class KorobAdmin(admin.ModelAdmin):
    list_display = ('korob_code', 'status', 'aggr', 'nanes',)
    list_filter = ('status', 'aggr', 'nanes',)