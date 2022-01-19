from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse
from inventory.forms import ProductForm
from django.http import HttpResponse
import csv


class ProductListView(generic.ListView):
    model = Product
    template_name = 'inventory/index.html'
    paginate_by = 20


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'inventory/detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/add_product.html'

    def get_success_url(self):
        return reverse('inventory:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/add_product.html'

    def get_success_url(self):
        return reverse('inventory:product-detail', args=[str(self.object.id)])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/delete.html'

    def get_success_url(self):
        return reverse('inventory:products')


def ExportCSV(request):
    products = Product.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=product.csv'
    writer = csv.writer(response)
    fields = [field.name for field in Product._meta.fields]
    writer.writerow(fields)
    rows = products.values_list()
    for r in rows:
        writer.writerow(r)
    return response
