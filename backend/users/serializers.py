from rest_framework import serializers
from .models import User, UserProfile


# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number']


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'role', 'last_login', 'profile']
        read_only_fields = ['id', 'last_login']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data)
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            instance.save()

        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        return instance