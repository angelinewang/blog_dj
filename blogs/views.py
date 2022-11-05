from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import redirect, HttpResponsePermanentRedirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from .forms import BlogForm
from rest_framework.reverse import reverse

# Create your views here.

# Class-based views makes these views even shorter

def home(request):
    data = {
        'app': 'Django'
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def blogs_list(request):
    # if request.method == 'GET':
    #     blogs = Blog.objects.all()
    #     serializer = BlogSerializer(blogs, many=True)
    #     # return JsonResponse(serializer.data, safe=False)
    #     return Response(serializer.data)

    # elif request.method == 'POST':
        # Must write raw JSON to submit data on the localhost website
        # Fields are not used

        # blog_data = {
        #     'title': request.data.get('title'),
        #     'description': request.data.get('description'),
        #     'content': request.data.get('content'),
        #     'author': request.data.get('author'),
        # }
        # blog_data = JsonResponse(request.data)

        context ={}

        form = BlogForm(request.POST or None)

        if form.is_valid():
            form.save()

        context['form']= form

        context['blogs']= BlogSerializer(Blog.objects.all())
        print(context)
        return render(request, "blogs_list.html", context)
        # serializer = BlogSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"data": serializer.data})

        # Find where the source code is...
        # djangorestframework installed in different folder, or folder in virtual env when the Python package is installed
        # virtualenvs folder on local folder: cd into the one for the current project, and in the bin folder
        
            # return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def blogs_detail_delete(request, pk):
    try: 
        context ={}
        obj = get_object_or_404(Blog, id=pk)
        context["data"] = BlogSerializer(Blog.objects.get(id = pk))
        # blog = Blog.objects.get(id=pk)
        # serializer = BlogSerializer(blog)
        # return Response(serializer.data)
    except Blog.DoesNotExist:
        return HttpResponse(status=302)
        
    if request.method == 'POST':
        obj.delete()
    
    return render(request, 'detail_view.html', context)

@api_view(['GET', 'POST'])
def update(request, pk):
    context ={}
    object = get_object_or_404(Blog, id=pk)
    final_obj = BlogSerializer(object)
    form = BlogForm(request.POST or None, instance = final_obj)

    if form.is_valid():
        form.save()

    context['form']= form

    return render(request, "update_view.html", context)

def redirect_view(request):
    response = redirect('blogs/')
    return response