from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from dailyjournalapi.models import Mood

class MoodView(ViewSet):
    """Viewset for moods """

    def list(self, request):
        mood = Mood.objects.all()

        serializer = MoodSerializer(
            mood, many=True, context={'requet': request}
        )
        return Response(serializer.data)

class MoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mood
        fields = ('id', 'label')
        depth = 1