
# import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),
] + debug_toolbar_urls()
