from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()

#VERSION 2 OF API (/api/v2/products)
router.register('products', ProductViewSet, basename='products')  # list, create, update and delete products

print(router.urls)

urlpatterns = router.urls