from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import (
    PeopleDetailViewSet,
    PeopleViewSet,
    PlanetViewSet,
    SpeciesViewSet,
    StarshipDetailViewSet,
    StarshipViewSet,
    UserViewSet,
)


router = routers.DefaultRouter()
router.register('people/detail', PeopleDetailViewSet)
router.register('people', PeopleViewSet)
router.register('starship/detail', StarshipDetailViewSet)
router.register('starship', StarshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
