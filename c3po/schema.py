import graphene
from c3po.models import C3POQuote
from c3po.chatbot import wernicke


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

    c3po_not_sure = graphene.List(
        graphene.String
    )
    def resolve_c3po_not_sure(self, info, **kwargs):
        '''
        Retorna os quotes para péssima idéias.
        '''
        quotes = quotes = C3POQuote.objects.all()
        return [quote.quote for quote in quotes if quote.is_not_sure]


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
        bad_idea = graphene.Boolean(
            required=False,
            description='Indicates if this is to be an bad ideia quote'
        )

    def mutate_and_get_payload(self, info, **_input):
        quote = _input.get('quote')
        bad_idea = _input.get('bad_idea', False)

        registry = C3POQuote.objects.create(quote=quote, is_not_sure=bad_idea)
        registry.save()
        return CreateC3POQuote(registry.quote)


class AskC3PO(graphene.relay.ClientIDMutation):
    response = graphene.String()
    class Input:
        question = graphene.String(required=True)
    def mutate_and_get_payload(self, info, **_input):
        question = _input.get('question', '')
        response = wernicke.get_response(question)
        return AskC3PO(str(response))


class Mutation:
    create_c3po_quote = CreateC3POQuote.Field()
    ask_c3po = AskC3PO.Field()
