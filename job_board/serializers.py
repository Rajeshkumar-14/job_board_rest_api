# serializers.py
from rest_framework import serializers
from .models import JobBoard


class JobBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobBoard
        fields = '__all__'