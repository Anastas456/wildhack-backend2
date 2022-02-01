from .models import Applications
from rest_framework import viewsets, permissions
from .serializers import ApplicationsSerializer


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Applications.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ApplicationsSerializer