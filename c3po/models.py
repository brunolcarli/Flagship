from django.db import models


class C3POQuote(models.Model):
    '''
    Quotes do C3PO
    '''
    quote = models.CharField(max_length=900, null=False, blank=False)
    quote_datetime = models.DateTimeField(auto_now_add=True)
    is_not_sure = models.BooleanField(default=False)
