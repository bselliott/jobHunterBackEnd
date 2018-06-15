from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=120,  blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    address = models.TextField(max_length=None, blank=True)
    job = models.ForeignKey("api.Job", on_delete=models.SET_NULL, null=True, blank=True)

    class JSONAPIMeta:
        resource_name = "people"


class Job(models.Model):
    job_type = models.CharField(max_length=50)
    job_title = models.CharField(max_length=75)
    company_name = models.CharField(max_length=120)
    company_address = models.TextField(max_length=None)
    job_description = models.TextField(max_length=None)

    class JSONAPIMeta:
        resource_name = "jobs"
