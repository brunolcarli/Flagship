import graphene
from bot.models import Quote

class Query(object):
    '''
    Queries da Lisa.
    '''
    check = graphene.String()
    def resolve_check(self, info, **kwargs):
        return 'hello daddy'

    bot_quotes = graphene.List(
        graphene.String,
        server_in=
    )
    def resolve_bot_quotes(self, info, **kwargs):
        return Quote.objects.filter(**kwargs)

class BotCreateQuote(graphene.relay.ClientIDMutation):
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
        return BotCreateQuote(registry.quote)

class Mutation:
    bot_create_quote = BotCreateQuote.Field()
