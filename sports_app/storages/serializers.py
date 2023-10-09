from rest_framework.serializers import ModelSerializer
from .models import FileUpload


# Serializers define the API representation.
class FileUploadSerializer(ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ["file"]

    def create(self, validated_data):
        print(validated_data)

        uploaded_file = validated_data["file"]
        # validate if the file incoming file is csv

        # decode csv file
        data = uploaded_file.read().decode('UTF-8')
        print(data)
        return super().create(validated_data)
