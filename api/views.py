from rest_framework import viewsets
from .models import Person, Job, Recruiter
from .serializers import PersonSerializer, JobSerializer, RecruiterSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Candidate to be CRUDed.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        if self.request.GET.get('job', True):
            return Person.objects.all()
        return Person.objects.filter(job=None)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        if self.request.GET.get('person', True):
            return Job.objects.all()
        return Job.objects.filter(person=None)


class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

    def get_queryset(self):
        if self.request.GET.get('person', True):
            return Recruiter.objects.all()
        return Recruiter.objects.filter(person=None)
