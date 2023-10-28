from abc import ABC

from rest_framework import serializers


class DateField(serializers.Field, ABC):
    def to_representation(self, value):
        return {
            'month': value.month,
            'day': value.day,
            'year': value.year
        }


class TimestampFieldSerializer(serializers.Field, ABC):
    def to_representation(self, value):
        if value:
            return round(value.timestamp() * 1000)
        else:
            return None


class ImageURLField(serializers.Field, ABC):
    def to_representation(self, value):
        if value:
            return value.url
        else:
            return None
