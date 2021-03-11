from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Profile
        fields = ['cell_phone_number','points']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name','email','password','profile']
    
    def create(self,validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data) 
        for attr, value in profile_data.items():
            setattr(user.profile, attr, value) 
        user.set_password(validated_data.get('password','SEPU123456'))        
        user.save()
        return user        
        
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        for attr, value in profile_data.items():
            setattr(instance.profile, attr, value)
        #instance.profile.save()    
        # 已在model add
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance 
