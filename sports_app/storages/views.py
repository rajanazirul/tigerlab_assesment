from rest_framework.response import Response
from .serializers import FileUploadSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.views import APIView
from .utils import FileUploadService


# ViewSets define the view behavior.
class FileUploadViewSet(APIView):
    serializer_class = FileUploadSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.validated_data["file"]

            # decode csv file
            datas = uploaded_file.read().decode("UTF-8")
            # Split the input data into rows
            rows = datas.strip().split("\n")

            for data in rows:
                # run process csv file input
                FileUploadService(data).process_match_input()

            # log csv data
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
