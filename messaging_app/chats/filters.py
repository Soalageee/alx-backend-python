import django_filters
from .models import Message
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class MessageFilter(django_filters.FilterSet):
    # Filter messages by sender
    sender_id = django_filters.UUIDFilter(field_name='sender__user_id')

    # Filter messages within a datetime range
    start_date = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender_id', 'start_date', 'end_date']