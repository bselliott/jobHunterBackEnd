from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Candidate to be CRUDed.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
