from rest_framework_json_api import serializers
from .models import Person, Job, Recruiter
from rest_framework_json_api.relations import ResourceRelatedField


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_type', 'job_title', 'company_name', 'company_address',
                  'job_description')


class PersonSerializer(serializers.ModelSerializer):
     job = ResourceRelatedField(
           queryset=Job.objects
           )

     class Meta:
        model = Person
        fields = "__all__"


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ('first_name', 'last_name', 'address', 'person')

    person = ResourceRelatedField(queryset=Person.objects, many=True)
