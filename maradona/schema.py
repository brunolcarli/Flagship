import graphene
from maradona.models import MaradonaScore


class MaradonaScoreType(graphene.ObjectType):
    player_name = graphene.String()
    steps = graphene.Int()
    game_datetime = graphene.DateTime()


class Query:
    maradona_scores = graphene.List(
        MaradonaScoreType,
        player_name=graphene.String(),
        steps__gte=graphene.Int(),
        steps__lte=graphene.Int(),
    )

    def resolve_maradona_scores(self, info, **kwargs):
        # if not filters return top 10:
        if not kwargs:
            return MaradonaScore.objects.order_by('steps')[:10]

        return MaradonaScore.objects.filter(**kwargs)


class CreateMaradonaScore(graphene.relay.ClientIDMutation):
    score = graphene.Field(MaradonaScoreType)

    class Input:
        player_name = graphene.String(required=True)
        steps = graphene.Int(required=True)

    def mutate_and_get_payload(self, info, **kwargs):
        score, _ = MaradonaScore.objects.get_or_create(
            player_name=kwargs['player_name'],
            steps=kwargs['steps']
        )
        score.save()

        return CreateMaradonaScore(score)


class Mutation:
    create_maradona_score = CreateMaradonaScore.Field()
