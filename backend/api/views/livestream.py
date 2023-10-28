from django.apps import apps
from django.http import JsonResponse
from rest_framework import generics

from backend.api import models, serializers


class GetLiveStream(generics.GenericAPIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        internal_data = models.InternalData.get_solo()
        kick = apps.get_app_config('api').kick

        return JsonResponse({
            'livestream': kick.livestream,
            'last_live': serializers.TimestampFieldSerializer().to_representation(internal_data.last_livestream)
        }, safe=False, status=200)
