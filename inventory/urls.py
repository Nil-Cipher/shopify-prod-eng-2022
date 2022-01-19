from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add/', views.ProductCreateView.as_view(), name='add-product'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='edit-product'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(),
         name='delete-product'),
    path('export/', views.ExportCSV, name='export-csv')
]
