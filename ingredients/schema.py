import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ingredients.models import Category
from graphql_relay.node.node import from_global_id 

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'descripcion','personas']
        interfaces = (relay.Node, )

class CreateCategory(graphene.relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)
    class Input:
        name = graphene.String()
        descripcion = graphene.String()
        personas = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        category = Category(
            name=input.get('name'),
            descripcion=input.get('descripcion'),
            personas=input.get('personas'),
        )
        category.save()
        return CreateCategory(category=category)


class UpdateCategory(graphene.relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)
    class Input:
        id = graphene.String()
        name = graphene.String()
        descripcion = graphene.String()
        personas = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        category = Category.objects.get(pk=from_global_id(input.get('id'))[1])
        category.name = input.get('name')
        category.descripcion = input.get('descripcion')
        category.personas = input.get('personas')
        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)

    class Input:
        id = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        category = Category.objects.get(pk=from_global_id(input.get('id'))[1])
        category.delete()
        return DeleteCategory(category=category)

class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

class Mutation(graphene.AbstractType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
