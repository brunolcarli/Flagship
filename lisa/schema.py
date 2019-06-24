import graphene

import bot.schema as bot

queries = (
    graphene.ObjectType,
    bot.Query,
)

mutations = (
    graphene.ObjectType,
    bot.Mutation,
)

class Query(*queries):
    pass


class Mutation(*mutations):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
