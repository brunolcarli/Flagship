import graphene

import bot.schema as bot

queries = (
    graphene.ObjectType,
    bot.Query,
)

class Query(*queries):
    pass

schema = graphene.Schema(query=Query)
