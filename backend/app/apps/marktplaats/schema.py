import graphene

from .models import CarListingModel
from .types import CarListingType
from .repositories import CarListingRepository

car_listing_repository = CarListingRepository()

class Query(graphene.ObjectType):
    car_listings = graphene.List(CarListingType, id = graphene.Int(required=False),
                                                 first = graphene.Int(required=False),
                                                 offset = graphene.Int(required=False))
    
    def resolve_car_listings(self, info, first=None, offset=None, **kwargs):
        return car_listing_repository.get(first=first, offset=offset, **kwargs)
        