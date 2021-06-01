from __future__ import unicode_literals

from django.db import models


class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    created = models.DateTimeField(auto_now_add=True, null=True)
    edited = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Planet(DateTimeModel):
    """ A planet i.e. Tatooine """

    name = models.CharField(max_length=100, null=True)
    rotation_period = models.CharField(max_length=40, null=True)
    orbital_period = models.CharField(max_length=40, null=True)
    diameter = models.CharField(max_length=40, null=True)
    climate = models.CharField(max_length=40, null=True)
    gravity = models.CharField(max_length=40, null=True)
    terrain = models.CharField(max_length=40, null=True)
    surface_water = models.CharField(max_length=40, null=True)
    population = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name


class People(DateTimeModel):
    """ A person i.e. - Luke Skywalker """

    name = models.CharField(max_length=100, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    mass = models.CharField(max_length=10, blank=True, null=True)
    hair_color = models.CharField(max_length=20, blank=True, null=True)
    skin_color = models.CharField(max_length=20, blank=True, null=True)
    eye_color = models.CharField(max_length=20, blank=True, null=True)
    birth_year = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=40, blank=True, null=True)
    homeworld = models.ForeignKey(Planet, related_name="residents", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Transport(DateTimeModel):

    name = models.CharField(max_length=40, null=True)
    model = models.CharField(max_length=40, null=True)
    manufacturer = models.CharField(max_length=80, null=True)
    cost_in_credits = models.CharField(max_length=40, null=True)
    length = models.CharField(max_length=40, null=True)
    max_atmosphering_speed = models.CharField(max_length=40, null=True)
    crew = models.CharField(max_length=40, null=True)
    passengers = models.CharField(max_length=40, null=True)
    cargo_capacity = models.CharField(max_length=40, null=True)
    consumables = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name


class Starship(Transport):
    """ A starship is a transport with a hypderdrive """

    hyperdrive_rating = models.CharField(max_length=40, null=True)
    MGLT = models.CharField(max_length=40, null=True)
    starship_class = models.CharField(max_length=40, null=True)
    pilots = models.ManyToManyField(
        People,
        related_name="starships",
        blank=True,
        null=True
    )


class Vehicle(Transport):
    """ A vehicle is anything without hyperdrive capability """

    vehicle_class = models.CharField(max_length=40, null=True)
    pilots = models.ManyToManyField(
        People,
        related_name="vehicles",
        blank=True,
        null=True
    )


class Species(DateTimeModel):
    "A species is a type of alien or person"

    name = models.CharField(max_length=40, null=True)
    classification = models.CharField(max_length=40, null=True)
    designation = models.CharField(max_length=40, null=True)
    average_height = models.CharField(max_length=40, null=True)
    skin_colors = models.CharField(max_length=200, null=True)
    hair_colors = models.CharField(max_length=200, null=True)
    eye_colors = models.CharField(max_length=200, null=True)
    average_lifespan = models.CharField(max_length=40, null=True)
    homeworld = models.ForeignKey(Planet, blank=True, null=True, on_delete=models.CASCADE)
    language = models.CharField(max_length=40, null=True)
    people = models.ManyToManyField(People, related_name="species", null=True)

    def __str__(self):
        return self.name


class Film(DateTimeModel):
    """ A film i.e. The Empire Strikes Back (which is also the best film) """

    title = models.CharField(max_length=100, null=True)
    episode_id = models.IntegerField(null=True)
    opening_crawl = models.TextField(max_length=1000, null=True)
    director = models.CharField(max_length=100, null=True)
    producer = models.CharField(max_length=100, null=True)
    release_date = models.DateField(null=True)
    characters = models.ManyToManyField(
        People,
        related_name="films",
        blank=True,
        null=True
    )
    planets = models.ManyToManyField(
        Planet,
        related_name="films",
        blank=True,
        null=True
    )
    starships = models.ManyToManyField(
        Starship,
        related_name="films",
        blank=True,
        null=True
    )
    vehicles = models.ManyToManyField(
        Vehicle,
        related_name="films",
        blank=True,
        null=True
    )
    species = models.ManyToManyField(
        Species,
        related_name="films",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
