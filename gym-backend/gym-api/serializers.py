from rest_framework import serializers
from .models import Workout, Exercise
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        extra_kwargs = {
            'image': {
                'required': True,
            }
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {
                'required': True,
                'write_only': True
            }
        }

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user = user)
            return user