from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.Serializer):

    class Meta:
        model = Feedback
        fields = (
            'user_id',
            'name',
            'email',
            'subject',
            'message',
            'created',
            'modified')