from rest_framework.routers import DefaultRouter

from order.views import OrderViewSet

urlpatterns = [
]

router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')

urlpatterns += router.urls
