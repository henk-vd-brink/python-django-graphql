from graphene_django import DjangoObjectType

from ..models import CarListingModel

class CarListingType(DjangoObjectType):
    class Meta: 
        model = CarListingModel