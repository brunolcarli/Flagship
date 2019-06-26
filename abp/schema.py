import graphene
from abp.models import Quote, Trainer, Badges


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
    badges = graphene.List(graphene.String)


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


class Mutation:
    create_abp_quote = CreateAbpQuote.Field()
    create_trainer = CreateTrainer.Field()
