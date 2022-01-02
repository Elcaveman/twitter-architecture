from django.contrib import admin
from django.urls import path,include

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user_data_manager.urls')),
    path('api/v1/',include('user_visibility.urls')),
    path('api/v1/',include('user_wizzard.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)