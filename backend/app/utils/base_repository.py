class BaseRepository:
    
    def _get_query_object(self):
        return self._model.objects
    
    def _handle_offset(self, result_query, offset_value):
        if offset_value:
            return result_query[offset_value::]
        return result_query
        
    def _handle_first(self, result_query, first_value):
        if first_value:
            return result_query[:first_value:]
        return result_query
        
    def _handle_kwargs(self, query_object, **kwargs):
        if not kwargs:
            return query_object.all()
            
        for i, (filter_type, filter_value) in enumerate(kwargs.items()):
            query_object = getattr(self, f"_filter_by_{filter_type}")(query_object, filter_value)
        return query_object.all()
            
    def get(self, first=None, offset=None, **kwargs):
        query_object = self._get_query_object()
        
        results = self._handle_kwargs(query_object, **kwargs)
        results = self._handle_offset(results, offset)
        return self._handle_first(results, first)