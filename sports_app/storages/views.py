from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get("file_uploaded")
        # content_type = file_uploaded.content_type
        print(file_uploaded)
        response = "POST API and you have uploaded a {} file"
        return Response(response)
