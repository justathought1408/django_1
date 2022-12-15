from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG

urlpatterns = [
    path('', include('app.app_urls')),
    path('admin/', admin.site.urls),
] 

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
