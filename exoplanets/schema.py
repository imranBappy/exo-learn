import graphene
from graphene_django.types import DjangoObjectType
from .models import Exoplanet


class ExoplanetType(DjangoObjectType):
    class Meta:
        model = Exoplanet


class ExoQuery(graphene.ObjectType):
    exoplanets = graphene.List(ExoplanetType)
    exoplanet  = graphene.Field(ExoplanetType, id=graphene.Int(required=True))

    def resolve_exoplanets(self):
        return Exoplanet.objects.all()
    
    def resolve_exoplanet(self, info, id):
        try:
            return Exoplanet.objects.get(pk=id)
        except Exoplanet.DoesNotExist:
            return None
    



