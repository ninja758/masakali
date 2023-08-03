from rest_framework import serializers
from .models import event, event_participation_record

class EventSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = event
        fields = ['id', 'start_time', 'end_time', 'result' ]

class EventParticipationRecordSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = event_participation_record
        fields = ['id', 'event', 'user', 'invested_money', 'user_benefit', 'timestamp']