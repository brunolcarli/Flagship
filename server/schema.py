import graphene

# import bot.schema as bot
import abp.schema as abp
# import r2d2.schema as r2d2
# import gomez.schema as gomez
import maradona.schema as maradona

queries = (
    graphene.ObjectType,
    bot.Query,
    abp.Query,
    r2d2.Query,
    gomez.Query,
    maradona.Query,
)

mutations = (
    graphene.ObjectType,
    bot.Mutation,
    abp.Mutation,
    r2d2.Mutation,
    gomez.Mutation,
    maradona.Mutation,
)

class Query(*queries):
    pass


class Mutation(*mutations):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
