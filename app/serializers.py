from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Film,
    People,
    Planet,
    Species,
    Starship,
    Vehicle,
)


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'starships']


class StarshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Starship
        fields = ['id', 'name', 'starship_class']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'name']


class PeopleDetailSerializer(serializers.HyperlinkedModelSerializer):
    starships = StarshipSerializer(many=True)
    vehicles = VehicleSerializer(many=True)

    class Meta:
        model = People
        fields = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'starships', 'vehicles']


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    homeworld = serializers.ReadOnlyField(source='homeworld.name')
    species = serializers.ReadOnlyField(source='species.name')

    class Meta:
        model = People
        fields = ['id', 'name', 'species', 'homeworld']


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain', 'surface_water', 'population']


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Species
        fields = ['name']


class StarshipDetailSerializer(serializers.HyperlinkedModelSerializer):
    films = FilmSerializer(many=True)
    pilots = PeopleSerializer(many=True)

    class Meta:
        model = Starship
        fields = ['id', 'name', 'model', 'cost_in_credits', 'length', 'crew', 'cargo_capacity', 'starship_class', 'pilots', 'films']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']
