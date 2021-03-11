from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers

from .models import Board, Post, Topic


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'topic']
        #fields = ['id', 'message', 'topic']


class ToCapitalizeCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.capitalize()


class TopicSerializer(serializers.ModelSerializer):    
    #board = serializers.StringRelatedField()
    starter = UserSerializer(read_only=True)     
    posts = PostSerializer(many=True, read_only=True)   
    days_since_create = serializers.SerializerMethodField()
    subject = ToCapitalizeCaseCharField()
    
    class Meta:
        model = Topic
        fields = ['id', 'board','subject','starter','description','created_at', 'views','posts','get_post_count','days_since_create']
        #fields = ['id', 'board','subject','description','created_at', 'views','posts','get_post_count','days_since_create']
    
    def get_days_since_create(self, obj):
        return (now() - obj.created_at).days



    def create(self, validated_data):       
        topic = Topic.objects.create(**validated_data)             
        return topic     



class BoardSerializer(serializers.ModelSerializer):    
    topics = serializers.SerializerMethodField()    
    class Meta:
        model = Board
        fields = ['id', 'name', 'description','get_posts_count','get_topics_count','get_last_post','topics']

    # def get_topics(self,obj):
    #     #boards/ api/^topic/query_topics\.(?P<format>[a-z0-9]+)/?$ [name='topic-query-topics']
    #     return "/boards/api/topic/query_topics?board={0}".format(obj.name)

    def get_topics(self,obj):
        #boards/ api/^topic/query_topics\.(?P<format>[a-z0-9]+)/?$ [name='topic-query-topics']
        return "/boards/{0}".format(obj.name)
