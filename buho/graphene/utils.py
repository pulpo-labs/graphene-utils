from graphene_django.types import DjangoObjectType
from graphql_geojson import GeoJSONType

class SoftDeleteDjangoObjectType:

    @classmethod
    def get_node(cls, info, id):
        queryset = cls.get_queryset(cls._meta.model.objects, info)
        try:
            return queryset.get(pk=id, trashed=False)
        except cls._meta.model.DoesNotExist:
            return None

class SoftDeleteGeoJSONType:
    
    @classmethod
    def get_node(cls, info, id):
        queryset = cls.get_queryset(cls._meta.model.objects, info)
        try:
            return queryset.get(pk=id, trashed=False)
        except cls._meta.model.DoesNotExist:
            return None

