import graphene
from abp.models import Quote, Trainer, Badges, Leader, Battle


class Roles(graphene.Enum):
    '''
    Define os cargos da liga
    '''
    GYM_LEADER = 'Gym Leader'
    ELITE_FOUR = 'Elite Four'
    CHAMPION = 'Champion'


class PokemonTypeTrainer(graphene.Enum):
    '''
    Define os tipos de pokémon que cada GL e E4 utilizam
    '''
    NORMAL = 'Normal'
    ROCK = 'Rock'
    ELECTRIC = 'Electric'
    GHOST = 'Ghost' 
    ICE = 'Ice'
    POISON = 'Poison' 
    WATER = 'Water'
    DARK = 'Dark'
    GRASS = 'Grass'
    DRAGON = 'Dragon'
    FIRE = 'Fire'
    BUG = 'Bug'
    FAIRY = 'Fairy'
    STEEL = 'Steel'
    PSYCHIC = 'Psychic'


class BadgeType(graphene.Enum):
    '''
    Define as insígnias da liga
    '''
    NORMAL = 'Normal'
    ROCK = 'Rock'
    ELECTRIC = 'Electric'
    GHOST = 'Ghost'
    ICE = 'Ice'
    POISON = 'Poison' 
    WATER = 'Water'
    DARK = 'Dark'
    GRASS = 'Grass'
    DRAGON = 'Dragon'
    PSYCHIC = 'Psychic'
    FAIRY = 'Fairy'

    @property
    def description(self):
        if self == Badge.DRAGON:
            return 'Dragon Badge;\nLeader: Bruno'
        return 'Other badge'


class Badge(graphene.ObjectType):
    '''
    Define a estrututa GraphQL para uma insígnia.
    '''
    id = graphene.ID(description='Badge ID')
    reference = BadgeType(
        description='Badge reference. i.e: Water, Normal, etc.'
    )


class LeaderType(graphene.ObjectType):
    '''
    Objeto GraphQl para um lider
    '''
    id = graphene.ID(
        description='Leader id'
    )
    nickname = graphene.String(
        description='Leader nickname'
    )
    num_wins = graphene.Int(
        description='Leader victory count'
    )
    num_losses = graphene.Int(
        description='Leader lose count'
    )
    num_battles = graphene.Int(
        description='Leader battle count'
    )
    battles = graphene.List(
        'abp.schema.BattleType',
        description='Battles this leader has participated'
    )
    pokemon_type = PokemonTypeTrainer(
        description='Pokemon type this leader use'
    )
    role = Roles(
        description='Leader role, i.e: Gym Leader, Elite Four, etc'
    )

    def resolve_battles(self, info, **kwargs):
        '''
        Retorna somente as batalhas que este líder esteve presente
        '''
        return Battle.objects.filter(battling_leader__exact=self)


class TrainerType(graphene.ObjectType):
    '''
    Objeto GraphQl para um Trainer.
    '''
    id = graphene.ID(
        description='Trainer ID'
    )
    nickname = graphene.String(
        description='Trainer nickname'
    )
    is_winner = graphene.Boolean(
        description='If player win the league champion, he is winner'
    )
    num_wins = graphene.Int(
        description='Trainer victory count'
    )
    num_losses = graphene.Int(
        description='Trainer lose count'
    )
    num_battles = graphene.Int(
        description='Trainer battle count'
    )
    badges = graphene.List(
        Badge,
        description='Badges this trainer has owned'
    )
    battles = graphene.List(
        'abp.schema.BattleType',
        description='Battles this trainer has participated'
    )

    def resolve_badges(self, info, **kwargs):
        '''
        Retornas as insígnias asssociadas à este treinador.
        '''
        return self.badges.all()

    def resolve_battles(self, info, **kwargs):
        '''
        Retorna as batalhas que este treiandor esteve presente
        '''
        return Battle.objects.filter(battling_trainer__exact=self)


class BattleType(graphene.ObjectType):
    '''
    Objeto Graphql para o registro de uma batalha
    '''
    trainer = graphene.Field(
        TrainerType,
        description='Trainer that is battling'
    )
    leader = graphene.Field(
        LeaderType,
        description='Leader that is battling'
    )
    winner = graphene.String(
        description='Ninckname of the winner'
    )
    battle_datetime = graphene.DateTime(
        description='Date that battle has occurred'
    )

    def resolve_trainer(self, info, **kwargs):
        '''
        Retorna o treinador que batalhou
        '''
        return self.battling_trainer

    def resolve_leader(self, info, **kwargs):
        '''
        Retorna o líder que batalhou
        '''
        return self.battling_leader

    def resolve_battle_datetime(self, info, **kwargs):
        '''
        Retorna a data da batalha
        '''
        return self.fight_date


class Score(graphene.ObjectType):
    '''
    Objeto GraphQL para o placar da liga
    '''
    trainers = graphene.List(
        TrainerType,
        description='Registered trainers'
    )

    def resolve_trainers(self, info, **kwargs):
        '''
        Retorna todos os treinadores
        '''
        return self


class Query(object):
    '''
    Queries para a aplicação ABP.
    '''

    abp_quotes = graphene.List(
        graphene.String,
        description='Query for ABP quotes registered by the Oak bot'
    )
    def resolve_abp_quotes(self, info, **kwargs):
        '''
        Retorna todos os quotes da ABP.
        '''
        quotes = Quote.objects.all()
        return [quote.quote for quote in quotes]

    abp_trainers = graphene.List(
        TrainerType,
        nickname=graphene.String(),
        description='Query for registered ABP trainers'
    )
    def resolve_abp_trainers(self, info, **kwargs):
        '''
        Retorna os treinadores registrados na liga
        '''
        nick = kwargs.get('nickname')

        # Filtre se o filtro foi fornecido
        if nick:
            response = Trainer.objects.filter(nickname=nick)
        else:
            response = Trainer.objects.all()
        return response

    abp_badges = graphene.List(
        Badge,
        description='Query for ABP badges'
    )
    def resolve_abp_badges(self, info, **kwargs):
        '''
        Retorna todas as insígnas da liga.
        '''
        badges = Badges.objects.all()
        return badges

    abp_leaders = graphene.List(
        LeaderType,
        nickname=graphene.String(),
        description='Query for registered ABP leaders'
    )
    def resolve_abp_leaders(self, info, **kwargs):
        '''
        Retorna todos os líderes registrados na liga ABP
        '''
        nick = kwargs.get('nickname')

        # Filtre se o filtro tiver sido fornecido
        if nick:
            response = Leader.objects.filter(nickname=nick)
        else:
            response = Leader.objects.all()
        return response

    abp_battles = graphene.List(
        BattleType,
        description='Query for registered ABP battles'
    )
    def resolve_abp_battles(self, info, **kwargs):
        '''
        Retorna todas as batalhas registradas na liga
        '''
        battles = Battle.objects.all()
        return battles

    # TODO - Isso pode muito bem ser adaptado ja que retorna somente todos
    # os trainers.
    abp_score_board = graphene.Field(Score)
    def resolve_abp_score_board(self, info, **kwargs):
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
        nickname = graphene.String()
        pokemon_type = PokemonTypeTrainer()
        role = Roles()

    def mutate_and_get_payload(self, info, **_input):
        nickname = _input.get('nickname')
        pokemon_type = _input.get('pokemon_type')
        role = _input.get('role')

        try:
            leader = Leader.objects.create(
                nickname=nickname,
                role=role,
                pokemon_type=pokemon_type
            )
        except Exception as ex:
            # TODO criar módulo de exceptions e levantar exception customizada
            raise Exception(ex)

        else:
            leader.save()

        return CreateLeader(leader)


class CreateTrainer(graphene.relay.ClientIDMutation):
    '''
    Registra um treinador no banco de dados.
    '''
    trainer = graphene.Field(TrainerType)

    class Input:
        nickname = graphene.String()

    def mutate_and_get_payload(self, info, **_input):
        nickname = _input.get('nickname')
    
        try:
            trainer = Trainer.objects.create(
                nickname=nickname,
            )

        except:
            raise Exception('Um treinador com este nome ja está cadastrado!')

        else:
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
        badge = _input.get('reference')
        if badge:
            try:
                created_badge = Badges.objects.create(reference=badge)

            except Exception:
                raise('Uma insígnia deste tipo ja foi cadastrada!')

            else:
                created_badge.save()

        else:
            raise Exception("Nenhuma insígnia fornecida.")

        return CreateBadge(created_badge)


class AddBadgeToTrainer(graphene.relay.ClientIDMutation):
    '''
    Adiciona uma insiígnia à um treinador.
    '''
    trainer = graphene.Field(TrainerType)

    class Input:
        badge = BadgeType()
        trainer = graphene.String()

    def mutate_and_get_payload(self, info, **_input):
        badge = _input.get('badge')
        trainer = _input.get('trainer')

        try:
            badge_to_give = Badges.objects.get(reference=badge)

        except Exception as ex:
            raise ex

        if badge_to_give:
            try:
                trainer = Trainer.objects.get(nickname=trainer)

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
