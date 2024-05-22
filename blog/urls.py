from django.urls import path
from .views import index, catalog, catalog_filter
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name='index'),
    path('catalog', catalog, name='catalog'),
    path('catalog/<int:kind_id>', catalog_filter, name='catalog_filter'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 