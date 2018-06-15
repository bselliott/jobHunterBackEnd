from rest_framework import viewsets
from .models import Person, Job
from .serializers import PersonSerializer, JobSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Candidate to be CRUDed.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
