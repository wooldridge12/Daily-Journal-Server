"""View module for handling requests about journalentries"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from dailyjournalapi.models import JournalEntry, Mood, Author

class JournalEntryView(ViewSet):
    """Daily Journal Entries"""

    def list(self, request):

        entries = JournalEntry.objects.all()

        serializer = EntrySerializer(
            entries, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        
        mood = Mood.objects.get(pk=request.data["mood"])

        entry = JournalEntry()
        entry.concept = request.data["concept"]
        entry.entry = request.data["entry"]
        entry.mood = mood
        entry.date = request.data["date"]
        

        try:
            entry.save()
            serializer = EntrySerializer(entry, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)




class EntrySerializer(serializers.ModelSerializer):
    """  """

    class Meta:
        """ """

        model = JournalEntry
        fields = ('id', 'concept', 'entry', 'mood', 'date')
        depth = 1