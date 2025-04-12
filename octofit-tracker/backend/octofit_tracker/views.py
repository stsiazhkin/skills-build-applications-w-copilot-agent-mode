from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

def get_base_url():
    # Dynamically determine the base URL for the API
    if settings.DEBUG:
        return "http://localhost:8000"
    return "https://potential-space-succotash-p7j7pj696v5365-8000.app.github.dev"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        base_url = get_base_url()
        return JsonResponse({"message": f"User API available at {base_url}/users/"})

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request, *args, **kwargs):
        base_url = get_base_url()
        return JsonResponse({"message": f"Team API available at {base_url}/teams/"})

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def list(self, request, *args, **kwargs):
        base_url = get_base_url()
        return JsonResponse({"message": f"Activity API available at {base_url}/activities/"})

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    def list(self, request, *args, **kwargs):
        base_url = get_base_url()
        return JsonResponse({"message": f"Leaderboard API available at {base_url}/leaderboard/"})

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def list(self, request, *args, **kwargs):
        base_url = get_base_url()
        return JsonResponse({"message": f"Workout API available at {base_url}/workouts/"})
