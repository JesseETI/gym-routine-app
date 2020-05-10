from rest_framework import serializers
from .models import Workout, Exercise
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'title', 'split', 'date', 'duration', 'author', 'author_name', 'exercises_list')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        extra_kwargs = {
            'image': {
                'required': True,
            }
        }

        def create(self, request, *args, **kwargs):
            response = {'message': 'Exercise cannot be created like this'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        print(user)
        Token.objects.create(user=user)
        return user