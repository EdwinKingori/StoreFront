from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from pprint import pprint

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.urls
pprint(router.urls)

urlpatterns = router.urls

# urlpatterns =[
#     # path('products/', views.ProductList.as_view(), name='product_list'),
#     # path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
#     # path('collections/', views.CollectionList.as_view(), name='collection-list'),
#     # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail')
# ]
