"""View module for handling requests about journalentries"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from dailyjournalapi.models import JournalEntry, Mood

class JournalEntryView(ViewSet):
    """Daily Journal Entries"""

    def list(self, request):

        entries = JournalEntry.objects.all()

        serializer = EntrySerializer(
            entries, many=True, context={'request': request})
        return Response(serializer.data)


class EntrySerializer(serializers.ModelSerializer):
    """  """

    class Meta:
        """ """

        model = JournalEntry
        fields = ('id', 'concept', 'entry', 'mood', 'date')
        depth = 1