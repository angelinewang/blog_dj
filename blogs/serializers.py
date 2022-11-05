from rest_framework import serializers
from .models import Blog
from comments.serializers import CommentSerializer
from users.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    author = UserSerializer(many=False, required=True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'content', 'author', 'comments')

    # def create(self, validated_data):
    #     blog = Blog.objects.create(**validated_data)
    #     return blog

    # def update(self, blog, validated_data):
    #     blog.title = validated_data.get("title", blog.title)
    #     blog.description = validated_data.get("description", blog.description)
    #     blog.content = validated_data.get("content", blog.content)
    #     blog.author = validated_data.get("author", blog.author)

    #     blog.save()
    #     return blog