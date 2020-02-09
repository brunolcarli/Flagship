import graphene
from bot.models import Quote

class Query(object):
    '''
    Queries da star destroyer.
    '''
    check = graphene.String()
    def resolve_check(self, info, **kwargs):
        return 'hello daddy'

    bot_quotes = graphene.List(
        graphene.String,
        server=graphene.String()
    )
    def resolve_bot_quotes(self, info, **kwargs):
        quotes = Quote.objects.filter(**kwargs)
        return [quote.quote for quote in quotes]

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
        server = graphene.String(
            description="Server where this messa was sent from"
        )

    def mutate_and_get_payload(self, info, **_input):
        registry = Quote.objects.create(**_input)
        registry.save()
        return BotCreateQuote(registry.quote)

class Mutation:
    bot_create_quote = BotCreateQuote.Field()
