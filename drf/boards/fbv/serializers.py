from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Topic

# class TopicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Topic
#         fields = ['id', 'subject', 'last_updated', 'starter', 'views']


class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject = serializers.CharField(required=False, allow_blank=True, max_length=100)
    starter = serializers.StringRelatedField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):    
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()       
        return instance
