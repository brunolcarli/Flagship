import graphene
from abp.models import Quote, Trainer, Badges, Leader, Battle


class Roles(graphene.Enum):
    GYM_LEADER = 'Gym Leader'
    ELITE_FOUR = 'Elite Four'
    CHAMPION = 'Champion'


class PokemonTypeTrainer(graphene.Enum):
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
    FIRE = 'Fire'
    BUG = 'Bug'
    FAIRY = 'Fairy'
    STEEL = 'Steel'


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
    battles = graphene.List('abp.schema.BattleType')
    pokemon_type = PokemonTypeTrainer()
    role = Roles()

    def resolve_battles(self, info, **kwargs):
        return Battle.objects.filter(battling_leader__exact=self)


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
    battles = graphene.List('abp.schema.BattleType')

    def resolve_badges(self, info, **kwargs):
        return self.badges.all()

    def resolve_battles(self, info, **kwargs):
        return Battle.objects.filter(battling_trainer__exact=self)


class BattleType(graphene.ObjectType):
    '''
    Objeto graphql para o registro de uma batalha
    '''
    trainer = graphene.Field(TrainerType)
    leader = graphene.Field(LeaderType)
    winner = graphene.String()
    battle_datetime = graphene.DateTime()

    def resolve_trainer(self, info, **kwargs):
        return self.battling_trainer

    def resolve_leader(self, info, **kwargs):
        return self.battling_leader

    def resolve_battle_datetime(self, info, **kwargs):
        return self.fight_date


class Score(graphene.ObjectType):
    '''
    Objeto GraphQL para o placar da liga
    '''
    trainers = graphene.List(TrainerType)

    def resolve_trainers(self, info, **kwargs):
        return self


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
    abp_trainers = graphene.List(
        TrainerType,
        nickname=graphene.String()
    )
    def resolve_abp_trainers(self, info, **kwargs):
        # TODO add docstring
        nick = kwargs.get('nickname')
        if nick:
            response = Trainer.objects.filter(nickname=nick)
        else:
            response = Trainer.objects.all()
        return response

    # TODO add description
    abp_badges = graphene.List(Badge)
    def resolve_abp_badges(self, info, **kwargs):
        # TODO add docstring
        badges = Badges.objects.all()
        return badges

    # TODO add description
    abp_leaders = graphene.List(
        LeaderType,
        nickname=graphene.String()
    )
    def resolve_abp_leaders(self, info, **kwargs):
        # TODO add docstring
        nick = kwargs.get('nickname')
        if nick:
            response = Leader.objects.filter(nickname=nick)
        else:
            response = Leader.objects.all()
        return response

    # TODO add description
    abp_battles = graphene.List(BattleType)
    def resolve_abp_battles(self, info, **kwargs):
        # TODO add docstring
        battles = Battle.objects.all()
        return battles

    # TODO add description
    abp_score_board = graphene.Field(Score)
    def resolve_abp_score_board(self, info, **kwargs):
        # TODO add docstring
        trainers = Trainer.objects.all()
        return trainers


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
        pokemon_type = PokemonTypeTrainer()
        role = Roles()

    def mutate_and_get_payload(self, info, **_input):
        name = _input.get('name')
        nickname = _input.get('nickname')
        pokemon_type = _input.get('pokemon_type')
        role = _input.get('role')

        leader = Leader.objects.create(
            name=name,
            nickname=nickname,
            role=role,
            pokemon_type=pokemon_type
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
        return AddBadgeToTrainer(trainer)


class CreateBattle(graphene.relay.ClientIDMutation):
    '''
    Registra uma batalha
    '''
    battle = graphene.Field(BattleType)

    class Input:
        trainer_nickname = graphene.String()
        leader_nickname = graphene.String()
        winner = graphene.String()

    def mutate_and_get_payload(self, info, **_input):

        trainer = _input.get('trainer_nickname')
        leader = _input.get('leader_nickname')
        winner = _input.get('winner')

        try:
            trainer = Trainer.objects.get(nickname=trainer)
        except Exception as ex:
            raise ex

        try:
            leader = Leader.objects.get(nickname=leader)
        except Exception as ex:
            raise ex

        if winner != trainer.nickname and winner != leader.nickname:
            raise Exception(
                'O vencedor deve ser um dos dois players fornecidos!'
            )
        else:
            if winner == trainer.nickname:
                trainer.num_wins += 1
                leader.num_losses += 1
            else:
                leader.num_wins += 1
                trainer.num_losses += 1

            trainer.num_battles += 1
            leader.num_battles += 1
            trainer.save()
            leader.save()

        if trainer and leader:
            battle = Battle.objects.create(
                battling_trainer=trainer,
                battling_leader=leader,
                winner=winner
            )
            battle.save()
            return CreateBattle(battle)
        else:
            raise Exception('Impossivel registrar batalha')


class Mutation:
    create_abp_quote = CreateAbpQuote.Field()
    create_trainer = CreateTrainer.Field()
    create_badge = CreateBadge.Field()
    add_badge_to_trainer = AddBadgeToTrainer.Field()
    create_leader = CreateLeader.Field()
    create_battle = CreateBattle.Field()
