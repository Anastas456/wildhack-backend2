from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from .serializers import ApplicationsSerializer
from django.http.response import JsonResponse
from rest_framework import status
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def volunteer_application_form(request):

    form_data = JSONParser().parse(request)
    form_serializer = ApplicationsSerializer(data=form_data)
    if form_serializer.is_valid():
        form_serializer.save()
        return JsonResponse(form_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)