from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from .views import *

# mapping urls
urlpatterns = [
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)