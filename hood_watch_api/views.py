from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def neighborhoodView(request):
    neighborhoods = Neighborhood.objects.all()
    serializer = NeighborhoodSerializer(neighborhoods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def neighborhoodDetail(request, pk):
    neighborhoods = Neighborhood.objects.get(id=pk)
    serializer = NeighborhoodSerializer(neighborhoods, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNeighborhood(request):
    serializer = NeighborhoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateNeighborhood(request, pk):
    neighborhood = Neighborhood.objects.get(pk=pk)
    serializer = NeighborhoodSerializer(instance=neighborhood, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNeighborhood(request, pk):
    neighborhood = Neighborhood.objects.get(pk=pk)
    neighborhood.delete()
    return Response("Neighborhood deleted successfully!")



# POST VIEWS
@api_view(['GET'])
def postView(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updatePost(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response("Post deleted successfully!")