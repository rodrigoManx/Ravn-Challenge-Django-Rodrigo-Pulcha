from __future__ import unicode_literals
import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug

from app import models


class Connection(graphene.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self.length


class Person(DjangoObjectType):
    '''An individual person or character within the Star Wars universe.'''
    class Meta:
        model = models.People
        exclude_fields = ('created', 'edited')
        filter_fields = ('name', )
        interfaces = (Node, )
        connection_class = Connection


class Planet(DjangoObjectType):
    '''A large mass, planet or planetoid in the Star Wars Universe,
    at the time of 0 ABY.'''
    climates = graphene.List(graphene.String)
    terrains = graphene.List(graphene.String)

    def resolve_climates(self, info):
        return [c.strip() for c in self.climate.split(',')]

    def resolve_terrains(self, info):
        return [c.strip() for c in self.terrain.split(',')]

    class Meta:
        model = models.Planet
        interfaces = (Node, )
        exclude_fields = ('created', 'edited', 'climate', 'terrain')
        filter_fields = ('name', )
        connection_class = Connection


class Film(DjangoObjectType):
    '''A single film.'''
    producers = graphene.List(graphene.String)

    def resolve_producers(self, info):
        return [c.strip() for c in self.producer.split(',')]

    class Meta:
        model = models.Film
        interfaces = (Node, )
        exclude_fields = ('created', 'edited', 'producer')
        filter_fields = {'episode_id': ('gt', )}
        connection_class = Connection


class Species(DjangoObjectType):
    '''A type of person or character within the Star Wars Universe.'''
    eye_colors = graphene.List(graphene.String)
    hair_colors = graphene.List(graphene.String)
    skin_colors = graphene.List(graphene.String)

    def resolve_eye_colors(self, info):
        return [c.strip() for c in self.eye_colors.split(',')]

    def resolve_hair_colors(self, info):
        return [c.strip() for c in self.hair_colors.split(',')]

    def resolve_skin_colors(self, info):
        return [c.strip() for c in self.skin_colors.split(',')]

    class Meta:
        model = models.Species
        interfaces = (Node, )
        exclude_fields = ('created', 'edited', 'eye_colors', 'hair_colors',
                          'skin_colors')
        filter_fields = ('name', )
        connection_class = Connection


class Vehicle(DjangoObjectType):
    '''A single transport craft that does not have hyperdrive capability'''
    manufacturers = graphene.List(graphene.String)

    def resolve_manufacturers(self, info):
        return [c.strip() for c in self.manufacturer.split(',')]

    class Meta:
        model = models.Vehicle
        interfaces = (Node, )
        exclude_fields = ('created', 'edited', 'manufacturers')
        filter_fields = {'name': {'startswith'}}
        connection_class = Connection


class Starship(DjangoObjectType):
    '''A single transport craft that has hyperdrive capability.'''
    manufacturers = graphene.List(graphene.String)

    def resolve_manufacturers(self, info):
        return [c.strip() for c in self.manufacturer.split(',')]

    def resolve_max_atmosphering_speed(self, info):
        if self.max_atmosphering_speed == 'n/a':
            return None
        return self.max_atmosphering_speed

    class Meta:
        model = models.Starship
        interfaces = (Node, )
        exclude_fields = ('created', 'edited', 'manufacturers')
        filter_fields = {'name': {'startswith', 'contains'}}
        connection_class = Connection


class Query(graphene.ObjectType):
    all_films = DjangoFilterConnectionField(Film)
    all_species = DjangoFilterConnectionField(Species)
    all_people = DjangoFilterConnectionField(Person)
    all_vehicles = DjangoFilterConnectionField(Vehicle)
    all_planets = DjangoFilterConnectionField(Planet)
    all_starships = DjangoFilterConnectionField(Starship)
    film = Node.Field(Film)
    species = Node.Field(Species)
    person = Node.Field(Person)
    vehicle = Node.Field(Vehicle)
    planet = Node.Field(Planet)
    starship = Node.Field(Starship)
    node = Node.Field()


schema = graphene.Schema(
    query=Query,
)
