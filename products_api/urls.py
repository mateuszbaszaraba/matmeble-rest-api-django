from .views import ProductsView, ProductDetail
from django.urls import path

app_name = 'products_api'

urlpatterns = [
    path('', ProductsView.as_view(), name='listproduct'),
    path('details/<str:pk>/', ProductDetail.as_view(), name='detailproduct'),
]
