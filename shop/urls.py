from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet,
                      basename='cart-items-detail')

urlpatterns = router.urls + products_router.urls + carts_router.urls


# urlpatterns =[
#     # path('products/', views.ProductList.as_view(), name='product_list'),
#     # path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
#     # path('collections/', views.CollectionList.as_view(), name='collection-list'),
#     # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail')
# ]
