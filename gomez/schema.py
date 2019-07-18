import graphene
from gomez.models import GomezQuote
from gomez.chatbot import wernicke


class Query(object):
    '''
        Queries do Gomez
    '''

    gomez_quotes = graphene.List(graphene.String)
    def resolve_gomez_quotes(self, info, **kwargs):
        '''
            Retorna todos os quotes do Gomez
        '''
        # return ['4c49534120534849454c4420424c4f434b494e47204841434b455220434f4e4e454354494f4e2e20786f786f203a2a']
        quotes = GomezQuote.objects.all()
        return [quote.quote for quote in quotes]


class CreateGomezQuote(graphene.relay.ClientIDMutation):
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

        registry = GomezQuote.objects.create(quote=quote)
        registry.save()
        return CreateGomezQuote(registry.quote)


class AskGomez(graphene.relay.ClientIDMutation):
    response = graphene.String()
    class Input:
        question = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **_input):
        question = _input.get('question', '')
        response = wernicke.get_response(question)
        return AskGomez(str(response))


class Mutation:
    create_gomez_quote = CreateGomezQuote.Field()
    ask_gomez = AskGomez.Field()
