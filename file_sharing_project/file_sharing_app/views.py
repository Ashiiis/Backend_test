from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from file_sharing_app.models import File
from file_sharing_app.serializers import FileSerializer

class FileUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class FileDownloadView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
