from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    # path('users/', include('custom_user.urls')),
    path('products/', include('product.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
