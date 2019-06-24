import graphene


class Query(object):
    '''
    Queries da Lisa.
    '''
    check = graphene.String()
    def resolve_check(self, info, **kwargs):
        return 'hello daddy'
