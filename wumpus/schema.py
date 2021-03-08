import graphene
from wumpus.models import WumpusScore


class WumpusScoreType(graphene.ObjectType):
    player_name = graphene.String()
    performance = graphene.Int()
    rounds = graphene.Int()
    game_datetime = graphene.DateTime()


class Query:
    wumpus_scores = graphene.List(
        WumpusScoreType,
        player_name=graphene.String(),
        performance__gte=graphene.Int(),
        performance__lte=graphene.Int(),
        rounds__gte=graphene.Int(),
        rounds__lte=graphene.Int(),
    )

    def resolve_wumpus_scores(self, info, **kwargs):
        # if not filters return top 10:
        if not kwargs:
            return WumpusScore.objects.order_by('-performance')[:10]

        return WumpusScore.objects.filter(**kwargs)


class CreateWumpusScore(graphene.relay.ClientIDMutation):
    score = graphene.Field(WumpusScoreType)

    class Input:
        player_name = graphene.String(required=True)
        performance = graphene.Int(required=True)
        rounds = graphene.Int(requried=True)

    def mutate_and_get_payload(self, info, **kwargs):
        if kwargs['performance'] >= 1000:
            raise Exception('Invalid score. Please dont try to hack the ranking.')

        score, _ = WumpusScore.objects.get_or_create(
            player_name=kwargs['player_name'],
            performance=kwargs['performance'],
            rounds=kwargs['rounds'],
        )
        score.save()

        return CreateWumpusScore(score)


class Mutation:
    create_wumpus_score = CreateWumpusScore.Field()
