from rest_framework.serializers import ModelSerializer
from .models import FileUpload


# Serializers define the API representation.
class FileUploadSerializer(ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ["file"]

    def create(self, validated_data):
        uploaded_file = validated_data["file"]
        # validate if the file incoming file is csv
        # if uploaded_file.name == ".csv"

        return super().create(validated_data)
