import graphene
from gomez.models import GomezQuote
# from gomez.chatbot import wernicke


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
