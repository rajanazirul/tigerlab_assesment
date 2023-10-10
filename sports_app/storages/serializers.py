from rest_framework.serializers import ModelSerializer
from .models import FileUpload


# Serializers define the API representation.
class FileUploadSerializer(ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ["file"]
