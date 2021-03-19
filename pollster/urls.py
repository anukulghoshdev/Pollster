from django.contrib import admin
from django.urls import path, include 
from user_reg import urls

from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls',namespace='polls')),
    path('registration/',include('user_reg.urls',namespace='user_reg')),
    path('login/',include('user_login.urls',namespace='user_login')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]

if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
