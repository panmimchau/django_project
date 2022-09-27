# serializer - serializowanie - zamiana obiektu na json'a
from .models import Idea, Vote
from rest_framework import serializers


#musimy stworzyc clase z dopiskiem serializer
class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'youtube_url', 'status']

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ['idea', 'reason']