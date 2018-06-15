from rest_framework_json_api import serializers
from .models import Person, Job
from rest_framework_json_api.relations import ResourceRelatedField


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'address', 'job')

    job = ResourceRelatedField(
            queryset=Job.objects,
            many=False,
            )


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_type', 'job_title', 'company_name', 'company_address',
                  'job_description')
