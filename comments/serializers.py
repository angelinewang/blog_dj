from rest_framework import serializers

from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, required=True)
    class Meta:
        model = Comment 
        field = '__all__'
