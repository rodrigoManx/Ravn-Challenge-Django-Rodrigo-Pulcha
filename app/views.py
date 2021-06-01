from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import (
    PeopleDetailSerializer,
    PeopleSerializer,
    PlanetSerializer,
    SpeciesSerializer,
    StarshipDetailSerializer,
    StarshipSerializer,
    UserSerializer,
)
from .models import (
    People,
    Planet,
    Species,
    Starship,
)


def index(request):
    return HttpResponse("Hello, world.")


class PeopleDetailViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleDetailSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class StarshipDetailViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = StarshipDetailSerializer


class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer