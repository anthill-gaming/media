import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from media import models


class RootQuery(graphene.ObjectType):
    pass


# noinspection PyTypeChecker
schema = graphene.Schema(query=RootQuery)
