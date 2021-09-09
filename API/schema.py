from  graphene import ObjectType, relay
import graphene
from graphene.types import interface
from graphene_django import DjangoObjectType, fields
from .models import Category, Sauce
from graphene_django.filter import DjangoFilterConnectionField
from .relaySchema import *


# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value='Hi, am Gerald')

# To create GraphQL types for each of our Django models, we are going to subclass the
#  DjangoObjectType class which will automatically 
# define GraphQL fields that correspond to the fields on the Django models.

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['id', 'name'] # works for basic tutorial
class SauceType(DjangoObjectType):
    class Meta:
        model = Sauce
        fields = ['id','name', 'notes', 'category'] # works for basic tutorial

# FOR BASIC TUTORIAL
class Query(ObjectType):
    all_sauce = graphene.List(SauceType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_sauce(root, info):
        # We can easily optimize query count in the resolve method
        return Sauce.objects.select_related('category').all()

    def resolve_category_by_name(root,info,name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


# tryna link Relay schema
class Query(QueryNode, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)