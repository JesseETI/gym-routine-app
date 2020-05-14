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
    permission_classes = (permissions.IsAuthenticated,)

    @action(methods=['GET'], detail = False)
    def getmyworkouts(self, request):
        user = request.user

        try:
            workout_queryset = Workout.objects.filter(author = user.id)
            serializer = WorkoutSerializer(workout_queryset, many = True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            response = {
                "message": "No workouts found",
            }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def getrelatedexercises(self, request, pk = None):

        try:
            workout = Workout.objects.get(id=pk)
            exercise_queryset = Exercise.objects.filter(workout = workout.id)

            serializer = ExerciseSerializer(exercise_queryset, many=True, context={"request": request})

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            response = {
                "message": "No exercises found"
            }

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def getcurrentuser(self, request):
        user = request.user

        try:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            response = {
                "message": "No user found",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['POST'], detail = True)
    def addExercise(self, request, pk = None):

        if 'reps' in request.data:
            workout = Workout.objects.get(id = pk)
            title = request.data['title']
            reps = request.data['reps']
            sets = request.data['sets']
            image = request.data['image']

            try:
                exercise = Exercise.objects.get(workout = workout.id)
                exercise.title = title
                exercise.reps = reps
                exercise.sets = sets
                exercise.image = image
                exercise.save()

                serializer = ExerciseSerializer(exercise, many=False)
                response = {
                    "message": "Exercise has been updated",
                    "result": serializer.data
                }
                return Response(response, status = status.HTTP_200_OK)
            except:
                exercise = Exercise.objects.create(title = title, sets = sets, reps = reps, image = image, workout = workout)
                serializer = ExerciseSerializer(exercise)
                response = {
                    "message": "Exercise has been added",
                    "result": serializer.data
                }
                return Response(response, status = status.HTTP_200_OK)
        else:
            response = {
                "message": "Please enter an exercise",
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