from django.apps import apps
from django.http import JsonResponse

from rest_framework import generics

from backend.api import serializers


class GetLeaderboards(generics.GenericAPIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        leaderboards = {}

        for leaderboard in apps.get_app_config('api').leaderboards:
            leaderboards[leaderboard.leaderboard_id] = {
                'entries': leaderboard.entries,
                'prizes': leaderboard.prizes,
                'end_at': leaderboard.end_at.timestamp() * 1000.0,
                'sort_field': leaderboard.sort_field,
                'updated_at': serializers.TimestampFieldSerializer().to_representation(leaderboard.updated_at)
            }


        
        return JsonResponse({
            'leaderboards': leaderboards
        }, safe=False, status=200)
