from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from nserver.models import Post
from rest_framework import viewsets
from nserver.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import exceptions

def index(request):
    latest_posts = Post.objects.order_by('PublishDate')
    output = ', '.join([p.Title for p in latest_posts])
    template = loader.get_template('nserver/index.html')
    context={
        'latest_posts' : latest_posts,
    }
    return HttpResponse(template.render(context,request))
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('PublishDate')
    serializer_class = PostSerializer

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all().order_by('PublishDate')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        username=request.user.username
        password=request.user.password
        user = authentificate(username=username,password=password)
        if user is None:
            raise exceptions.AuthenticationFailed('No such user')
        post = self.get_object(pk)
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        
        username=request.user.username
        password=request.user.password
        user = authentificate(username=username,password=password)
        if user is None:
            raise exceptions.AuthenticationFailed('No such user')

        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)