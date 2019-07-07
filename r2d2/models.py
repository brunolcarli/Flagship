r'''
R2D2 DATABASE MODELS

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
         `---'
'''
from django.db import models

class R2QuoteModel(models.Model):
    '''
    Stores quotes for civil cultural project on discord.
    '''
    quote = models.CharField(max_length=600, null=False, blank=False)
