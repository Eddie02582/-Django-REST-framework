from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Topic


class TopicSerializer(serializers.ModelSerializer):
    #posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'subject', 'last_updated', 'starter', 'views','posts']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'topic']
        #fields = ['id', 'message', 'topic']
