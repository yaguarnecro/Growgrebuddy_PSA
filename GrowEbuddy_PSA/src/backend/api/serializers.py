# src/backend/api/serializers.py

from rest_framework import serializers
from .models import Vpet  # Import the Vpet model

class VpetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vpet
        fields = ['vpet_id', 'user_id', 'level', 'experience_points', 'mood']  # Adjust fields as necessary