from decimal import Context
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, generics, mixins, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
import requests
import json
import uuid
import time

# Create your views here.

class TestAAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'message': 'Hello World!'})


