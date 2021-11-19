import graphene

from .models import CarListingModel
from .types import CarListingType
from .repositories import CarListingRepository

class Query(graphene.ObjectType):
    car_listings = graphene.List(CarListingType, first = graphene.Int(required=False),
                                                    offset = graphene.Int(required=False))
    
    def resolve_car_listings(self, info, first=None, offset=None, **kwargs):
        return "joejoe"
        