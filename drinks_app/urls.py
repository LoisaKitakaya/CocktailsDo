from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
# from django.conf.urls import handler404
from .views import *

# mapping urls
urlpatterns = [
    path('', base, name='base'),
    path('drinks', home, name='home'),    
]

handler404 = 'drinks_app.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)