from rest_framework_json_api import serializers
from .models import Person
# from rest_framework_json_api.relations import ResourceRelatedField


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'address')
