from rest_framework import serializers
from nserver.models import Post
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['Title','Abstract','FullText','ImageUrl','PublishDate','UrlTitle']