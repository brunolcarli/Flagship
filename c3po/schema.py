import graphene
from c3po.models import C3POQuote

class Query(object):
    '''
    Queries do C3PO
    '''

    c3po_quotes = graphene.List(graphene.String)
    def resolve_c3po_quotes(self, info, **kwargs):
        '''
        Retorna todos os quotes do C3PO
        '''
        quotes = C3POQuote.objects.all()
        return [quote.quote for quote in quotes]


class CreateC3POQuote(graphene.relay.ClientIDMutation):
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
        registry = C3POQuote.objects.create(quote=quote)
        registry.save()
        return CreateC3POQuote(registry.quote)


class Mutation:
    create_c3po_quote = CreateC3POQuote.Field()
