from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from .views import *

# mapping urls
urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)