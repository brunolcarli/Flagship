import graphene
from abp.models import Quote, Trainer, Badges, Leader


class BadgeType(graphene.Enum):
    NORMAL = 'Normal'
    ROCK = 'Rock'
    ELECTRIC = 'Electric'
    GHOST = 'Ghost' 
    ICE = 'Ice'
    POISON = 'Poison' 
    WATER = 'Water'
    DARK = 'Dark'
    GRASS = 'Grss'
    DRAGON = 'Dragon'

    @property
    def description(self):
        if self == Badge.DRAGON:
            return 'Dragon Badge;\nLeader: Bruno'
        return 'Other badge'


class Badge(graphene.ObjectType):
    '''
    Define a estrututa GraphQL para uma insígnia.
    '''
    id = graphene.ID()
    reference = BadgeType()


class LeaderType(graphene.ObjectType):
    '''
    Objeto GraphQl para um lider
    '''
    id = graphene.ID()
    name = graphene.String()
    nickname = graphene.String()
    num_wins = graphene.Int()
    num_losses = graphene.Int()
    num_battles = graphene.Int()


class TrainerType(graphene.ObjectType):
    '''
    Objeto GraphQl para um Trainer.
    '''
    id = graphene.ID()
    name = graphene.String()
    nickname = graphene.String()
    is_winner = graphene.Boolean()
    num_wins = graphene.Int()
    num_losses = graphene.Int()
    num_battles = graphene.Int()
    badges = graphene.List(Badge)

    def resolve_badges(self, info, **kwargs):
        return self.badges.all()


class Query(object):
    '''
    Queries para a aplicação ABP.
    '''
    # TODO add description
    abp_quotes = graphene.List(graphene.String)
    def resolve_abp_quotes(self, info, **kwargs):
        # TODO add docstring
        quotes = Quote.objects.all()
        return [quote.quote for quote in quotes]

    # TODO add description
    abp_trainers = graphene.List(TrainerType)
    def resolve_abp_trainers(self, info, **kwargs):
        # TODO add docstring
        trainers = Trainer.objects.all()
        return trainers

    # TODO add description
    abp_badges = graphene.List(Badge)
    def resolve_abp_badges(self, info, **kwargs):
        # TODO add docstring
        badges = Badges.objects.all()
        return badges

    # TODO add description
    abp_leaders = graphene.List(LeaderType)
    def resolve_abp_leaders(self, info, **kwargs):
        # TODO add docstring
        leaders = Leader.objects.all()
        return leaders


class CreateAbpQuote(graphene.relay.ClientIDMutation):
    '''
    Registra um quote no banco de dados.
    '''
    response = graphene.String(
        description='Create a text quote on the database.'
    )

    class Input:
        quote = graphene.String(
            required=True,
            description='A quote to be forever remembered.'
        )

    def mutate_and_get_payload(self, info, **_input):

        quote = _input.get('quote')
        registry = Quote.objects.create(quote=quote)
        registry.save()
        return CreateAbpQuote(registry.quote)

class CreateLeader(graphene.relay.ClientIDMutation):
    '''
    Registra um treinador no banco de dados.
    '''

    leader = graphene.Field(LeaderType)

    class Input:
        name = graphene.String()
        nickname = graphene.String()

    def mutate_and_get_payload(self, info, **_input):
        name = _input.get('name')
        nickname = _input.get('nickname')
        leader = Leader.objects.create(
            name=name,
            nickname=nickname,
        )

        leader.save()
        return CreateLeader(leader)



class CreateTrainer(graphene.relay.ClientIDMutation):
    '''
    Registra um treinador no banco de dados.
    '''

    trainer = graphene.Field(TrainerType)

    class Input:
        name = graphene.String()
        nickname = graphene.String()

    def mutate_and_get_payload(self, info, **_input):
        name = _input.get('name')
        nickname = _input.get('nickname')
        trainer = Trainer.objects.create(
            name=name,
            nickname=nickname,
        )

        trainer.save()
        return CreateTrainer(trainer)


class CreateBadge(graphene.relay.ClientIDMutation):
    '''
    Registra uma insígnia no banco de dados
    '''
    badge = graphene.Field(Badge)

    class Input:
        reference = BadgeType()

    def mutate_and_get_payload(self, info, **_input):
        # TODO add docstring
        badge = _input.get('reference')
        if badge:
            try:
                created_badge = Badges.objects.create(reference=badge)
                created_badge.save()
            except Exception as ex:
                raise(ex)
        else:
            raise Exception("None given")

        return CreateBadge(created_badge)


class AddBadgeToTrainer(graphene.relay.ClientIDMutation):
    '''
    Adiciona uma insiígnia à um treinador.
    '''
    trainer = graphene.Field(TrainerType)

    class Input:
        badge_id = graphene.ID()
        trainer_id = graphene.ID()

    def mutate_and_get_payload(self, info, **_input):
        # TODO add docstring
        badge_id = _input.get('badge_id')
        trainer_id = _input.get('trainer_id')

        try:
            badge_to_give = Badges.objects.get(id=badge_id)
        except Exception as ex:
            raise ex

        if badge_to_give:
            try:
                trainer = Trainer.objects.get(id=trainer_id)
            except Exception as ex:
                raise ex
            if trainer:
                trainer.badges.add(badge_to_give)
                trainer.save()
        return AddBadgeToTrainer    (trainer)


class Mutation:
    create_abp_quote = CreateAbpQuote.Field()
    create_trainer = CreateTrainer.Field()
    create_badge = CreateBadge.Field()
    add_badge_to_trainer = AddBadgeToTrainer.Field()
    create_leader = CreateLeader.Field()
