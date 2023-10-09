from rest_framework.serializers import Serializer
from .models import FileUpload


# Serializers define the API representation.
class FileUploadSerializer(Serializer):
    class Meta:
        model = FileUpload
        fields = ["file"]
