from utils import BaseRepository
from ..models import CarListingModel

class CarListingRepository(BaseRepository):
    _model = CarListingModel
    
    def _filter_by_id(self, object, value):
        return object.filter(id=value)