from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=666, null=False, blank=False)
