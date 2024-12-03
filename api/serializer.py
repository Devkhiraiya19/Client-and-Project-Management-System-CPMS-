from rest_framework import serializers
from api.models import Client, Project
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        models = Project
        fields = '__all__'
