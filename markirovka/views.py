from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import csv
from .forms import UploadItemCsvFileForm
from .models import Country, Product, Download_codes_files, Donwload_codes


def index(request):
    return HttpResponse('<h2> form submitted.</h2>')

class Download_codes(View):

    def my_view(request):

        if request.method == 'POST':
            form = UploadItemCsvFileForm(request.POST, request.FILES)
            if form.is_valid():
                country = Country.objects.filter(id=request.POST['country']).get()
                product = Product.objects.filter(id=request.POST['products']).get()
                newdoc = Download_codes_files(name=request.FILES['file'])

                newdoc.save()

                # Получить id записи и получить доступ к файлу и все коды залить в бд

                urk = Download_codes_files.objects.get(id=newdoc.id)


                with open(f'media/{urk.name}') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for code in csv_reader:
                        new_codes = Donwload_codes(code=str(code[0]), country=country, products=product)
                        new_codes.save()

                return redirect('admin:index')
            else:
                message = 'The form is not valid. Fix the following error:'
        else:
            form = UploadItemCsvFileForm()  # An empty, unbound form

        # Load documents for the list page
        documents = Download_codes_files.objects.all()

        # Render list page with the documents and the form
        context = {'documents': documents, 'form': form}
        return render(request, 'markirovka/index.html', context)