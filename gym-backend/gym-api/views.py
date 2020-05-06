from django.shortcuts import render
from rest_framework import viewsets
from .models import Workout, Exercise
from .serializers import WorkoutSerializer, ExerciseSerializer, UserSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    @action(methods=['POST'], detail = True)
    def addExercise(self, request, pk = None):
        if 'title' in request.data:
            workout = Workout.objects.get(id = pk)
            user = request.user
            title = request.data["title"]

            try:
                exercise = Exercise.objects.get(user = user.id, workout = workout.id)
                exercise.title = title
                exercise.save()

                serializer = ExerciseSerializer(exercise, many=False)
                response = {
                    "message": "Exercise has been updated",
                    "result": serializer.data
                }
                return Response(response, status = status.HTTP_200_OK)
            except:
                exercise = Exercise.objects.create(user = user, title = title)
                serializer = ExerciseSerializer(exercise)
                response = {
                    "message": "Exercise has been added",
                    "result": serializer.data
                }
                return Response(response, status = status.HTTP_200_OK)
        else:
            response = {
                "message": "Please enter a title (img not implemented yet) for the exercise",
            }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)