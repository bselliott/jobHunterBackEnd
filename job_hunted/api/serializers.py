from rest_framework_json_api import serializers
from .models import Person, Job, Recruiter
from rest_framework_json_api.relations import ResourceRelatedField


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'address',)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_type', 'job_title', 'company_name', 'company_address',
                  'job_description')


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ('first_name', 'last_name', 'address')
