from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

admin.site.site_header = 'StoreFront Admin'
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('playground.urls')),
    path('shop/', include('shop.urls')),
] + debug_toolbar_urls()
