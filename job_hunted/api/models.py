from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=120,  blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    address = models.TextField(max_length=None, blank=True)

    class JSONAPIMeta:
        resource_name = "persons"
