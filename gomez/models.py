from django.db import models

class GomezQuote(models.Model):
    '''
    Quotes do Gomez
    '''
    quote = models.CharField(max_length=900, null=False, blank=False)
    quote_datetime = models.DateTimeField(auto_now_add=True)
