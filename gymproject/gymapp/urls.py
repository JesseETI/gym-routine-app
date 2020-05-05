from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import WorkoutViewSet, ExerciseViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('workouts', WorkoutViewSet)
router.register('exercises', ExerciseViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]