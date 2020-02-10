from django.db import models


class Quote(models.Model):
    quote = models.TextField(null=False, blank=False)
    server = models.CharField(max_length=100, null=True, blank=True)
