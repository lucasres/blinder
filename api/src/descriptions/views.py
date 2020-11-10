from django.shortcuts import render
from rest_framework import generics
from descriptions.serializers import CreateDescriptionSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateDescriptionView(generics.CreateAPIView):
    serializer_class = CreateDescriptionSerializer
    permission_classes = [IsAuthenticated,]
    #authentication_classes = [BasicAuthentication,]

create_description = CreateDescriptionView.as_view()