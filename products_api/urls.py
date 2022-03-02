from .views import Products
from rest_framework.routers import DefaultRouter

app_name = 'products_api'

router = DefaultRouter()
router.register('', Products, basename='products')

urlpatterns = router.urls
