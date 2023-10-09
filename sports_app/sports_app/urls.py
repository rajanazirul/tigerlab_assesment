from django.contrib import admin
from django.urls import path, include
from storages.views import FileUploadViewSet
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('upload/', FileUploadViewSet.as_view(), name='upload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)