from rest_framework import serializers
from .models import Task
from django.utils import timezone
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    