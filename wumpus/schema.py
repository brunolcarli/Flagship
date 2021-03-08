import graphene
from wumpus.models import WumpusScore


class WumpusScoreType(graphene.ObjectType):
    player_name = graphene.String()
    performance = graphene.Int()
    rounds = graphene.Int()
    game_datetime = graphene.DateTime()


class Query:
    wumpus_scores = graphene.List(WumpusScoreType)

    def resolve_wumpus_scores(self, info, **kwargs):
        return WumpusScore.objects.all()
