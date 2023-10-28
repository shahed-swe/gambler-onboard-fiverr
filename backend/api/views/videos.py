from django.apps import apps
from django.http import JsonResponse

from rest_framework import generics


class GetVideos(generics.GenericAPIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        youtube = apps.get_app_config('api').youtube

        return JsonResponse({
            'videos': youtube.entries
        }, safe=False, status=200)
