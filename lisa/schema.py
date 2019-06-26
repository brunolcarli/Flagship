import graphene

import bot.schema as bot
import abp.schema as abp

queries = (
    graphene.ObjectType,
    bot.Query,
    abp.Query
)

mutations = (
    graphene.ObjectType,
    bot.Mutation,
    abp.Mutation
)

class Query(*queries):
    pass


class Mutation(*mutations):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
