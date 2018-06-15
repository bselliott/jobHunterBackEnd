from rest_framework import viewsets
from .models import Person, Job, Recruiter
from .serializers import PersonSerializer, JobSerializer, RecruiterSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Candidate to be CRUDed.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
