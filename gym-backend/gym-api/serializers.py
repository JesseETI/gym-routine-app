from rest_framework import serializers
from .models import Workout, Exercise
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.fields import CurrentUserDefault


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'title', 'split', 'date', 'duration', 'author', 'author_name')

    def create(self, validated_data):
        user = self.context["request"].user
        workout = Workout.objects.create(**validated_data, author= user)
        return workout


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


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