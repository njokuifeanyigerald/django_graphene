from  graphene import ObjectType, relay
import graphene
from graphene.types import interface
from graphene_django import DjangoObjectType, fields
from .models import Category, Sauce
from graphene_django.filter import DjangoFilterConnectionField


class CategoryRelayNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'sauce']
        interfaces = (relay.Node, )

class SauceRelayNode(DjangoObjectType):
    class Meta:
        model = Sauce
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact','icontains','istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact']
        }
        interfaces = (relay.Node,)



class QueryNode(graphene.ObjectType):
    category  = relay.Node.Field(CategoryRelayNode) 
    all_categories = DjangoFilterConnectionField(CategoryRelayNode)

    sauce = relay.Node.Field(SauceRelayNode)
    all_sauce = DjangoFilterConnectionField(SauceRelayNode)

