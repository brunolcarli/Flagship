import graphene

import bot.schema as bot
import abp.schema as abp
import r2d2.schema as r2d2
import maradona.schema as maradona
import wumpus.schema as wumpus


queries = (
    graphene.ObjectType,
    bot.Query,
    abp.Query,
    r2d2.Query,
    maradona.Query,
    wumpus.Query
)

mutations = (
    graphene.ObjectType,
    bot.Mutation,
    abp.Mutation,
    r2d2.Mutation,
    maradona.Mutation,
    wumpus.Mutation
)

class Query(*queries):
    pass


class Mutation(*mutations):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
