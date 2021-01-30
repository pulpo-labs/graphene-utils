from graphene_django.types import DjangoObjectType
from graphql_geojson import GeoJSONType

class SoftDeleteDjangoObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def get_queryset(cls, queryset, info):
        queryset = queryset.filter(trashed=False)
        return queryset


class SoftDeleteGeoJSONType(GeoJSONType):
    class Meta:
        abstract = True
    
    @classmethod
    def get_queryset(cls, queryset, info):
        queryset = queryset.filter(trashed=False)
        return queryset
