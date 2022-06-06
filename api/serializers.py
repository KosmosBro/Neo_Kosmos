from rest_framework import serializers

from main.models import Person


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'img', 'name', 'age', 'address']
