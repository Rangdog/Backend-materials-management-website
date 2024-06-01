from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'depot', Depotviewset)
router.register(r'profile', Profileviewset)
router.register(r'business_Partner', BusinessPartnerviewset)
router.register(r'category', Categoryviewset)
router.register(r'product', Productviewset)
router.register(r'product_depot', ProductDepotviewset)
router.register(r'pricelist', Pricelistviewset)
router.register(r'product_price', ProductPriceviewset)
router.register(r'order_form', OrderFormviewset)
router.register(r'order_detail', OrderDetailviewset)
router.register(r'import_form', ImportFormviewset)
router.register(r'import_detail', ImportDetailviewset)
router.register(r'export_form', Export_Form_viewset)
router.register(r'export_detail', Export_Detail_viewset)

urlpatterns = [
    path('', include(router.urls)),
    path('password_reset/', views.CustomResetPasswordRequestToken.as_view()),
    path('password_reset/confirm/', views.CustomResetPasswordConfirmView.as_view()),
]
