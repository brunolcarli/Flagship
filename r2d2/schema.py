r'''
R2D2 SCHEMA

         _____
       .'/L|__`.
      / =[_]O|` \
      |"+_____":|__
   ||[] ||====| []||
   ||[] | |=| | []||
   |:||_|=|U| |_||:|
   | |||] [_][]C|| |
   | ||-'"""""`-|| |
   /|\\_\_|_|_/_//|\
  |___|   /|\   |___| 
  `---'  |___|  `---' 
'''
import graphene
from r2d2.models import R2QuoteModel


class Query(object):
    '''
    Queries for R2D2 Discord Bot
    '''
    r2_quotes = graphene.List(
        graphene.String,
        description='List of civil cultural discord quotes'
    )
    def resolve_r2_quotes(self, info, **kwargs):
        '''
        Returns all quotes from civil cultural registered by the
        R2D2 Bot.
        '''
        quotes = R2QuoteModel.objects.all()
        return [quote.quote for quote in quotes]


class CreateR2Quote(graphene.relay.ClientIDMutation):
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
        registry = R2QuoteModel.objects.create(quote=quote)
        registry.save()
        return CreateR2Quote(registry.quote)


class Mutation:
    create_r2_quote = CreateR2Quote.Field()
