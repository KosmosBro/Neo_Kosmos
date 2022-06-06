from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import PersonSerializers
from main.models import Person


class PersonListAPIView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
