from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog

# Create your views here.

def home(request):
    data = {
        'app': 'Django'
    }
    return JsonResponse(data)


@api_view(('GET',))
def blog_list(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(('POST'))
def blog_create(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
