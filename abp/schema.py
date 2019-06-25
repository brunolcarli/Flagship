import graphene

class Query(object):
    '''
    Queries para a aplicação ABP.
    '''
    teste = graphene.String()
    def resolve_teste(self, info, **kwargs):
        return 'ABP working'