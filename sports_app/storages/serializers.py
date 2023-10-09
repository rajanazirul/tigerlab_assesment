from rest_framework.serializers import Serializer, FileField


# Serializers define the API representation.
class FileUploadSerializer(Serializer):
    file = FileField()

    class Meta:
        fields = ["file"]
