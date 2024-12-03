from django.shortcuts import render
from api.models import Client, Project
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializer import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User

# Create your views here.
class ClientListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED )

class ClientDetailView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return None
        
    def get(self, request, pk):
        client = self.get_object(pk)   #Calls another function (get_object) to find the client with the given ID (pk).
        if not client:   # Checks if the client was found.If the client doesn’t exist (client is None), it sends an error response.
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client)  #If the client was found, this converts (serializes) the client data into JSON format so it can be sent in the response.
        return Response(serializer.data)
    
    def put(self, request, pk):
        client = self.get_object(pk) 
        if not client:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        client = self.get_object(pk)
        if not client:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

# PROJECT VIEWS
class ProjectListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProjectsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = request.user.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

