from .views import ProductList, ProductDetail, CreateProduct
from django.urls import path

app_name = 'products_api'

urlpatterns = [
    path('', ProductList.as_view(), name='listproduct'),
    path('details/<str:pk>/', ProductDetail.as_view(), name='detailproduct'),
    path('create/', CreateProduct.as_view(), name='createproduct'),
]
