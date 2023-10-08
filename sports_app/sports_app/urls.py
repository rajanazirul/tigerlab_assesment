from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from storages.views import UploadViewSet
router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('storages/', include(router.urls)),
]
