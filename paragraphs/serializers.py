# serializers.py

from rest_framework import serializers
from .models import Paragraph, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'dob', 'created_at', 'modified_at']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'content', 'words', 'created_at']
