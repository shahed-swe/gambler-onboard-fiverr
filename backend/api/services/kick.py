import httpx as httpx
from django.apps import apps


class Kick:
    channel_handle: str = None
    livestream: dict = None

    def __init__(self):
        self.channel_handle = None
        self.livestream = None

    def load(self):
        app_config = apps.get_app_config('api').app_config
        self.channel_handle = app_config

    def fetch_data(self):
        url = 'https://kick.com/api/v2/channels/thegambler1999'

        response = httpx.get(url=url)

        if response.status_code == 403:
            raise Exception('Failed to fetch livestream data from Kick - Unauthorized')
        if response.status_code != 200:
            print(response.status_code)
            raise Exception('Unhandled status code while fetching livestream data from Kick')

        self.livestream = response.json()['livestream']

        if self.livestream is not None:
            from django.utils import timezone
            from backend.api import models
            internal_data = models.InternalData.get_solo()
            internal_data.last_livestream = timezone.now()
            internal_data.save()
