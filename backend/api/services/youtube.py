import requests

from django.apps import apps


class YouTube:
    api_key: str = None
    channel_id: str = None
    entries: list = None

    def __init__(self):
        self.api_key = None
        self.channels = None
        self.entries = None

    def load(self):
        app_config = apps.get_app_config('api').app_config

        self.api_key = app_config['youtube']['api_key']
        self.channels = app_config['youtube']['channels']
        self.entries = []

    def fetch_data(self):
        print('Fetching YouTube data...')

        entries = []
        for channel_id in self.channels:
            print(f'Fetching channel data for {channel_id}')
            channel_data = self.fetch_channel_data(channel_id)

            print(f'Fetching uploaded videos for {channel_id}')
            videos_data = self.fetch_uploads(channel_data)

            for video in videos_data:
                if video['snippet']['title'].endswith('#shorts'):
                    continue

                if 'maxres' in video['snippet']['thumbnails']:
                    thumbnail = video['snippet']['thumbnails']['maxres']
                else:
                    thumbnail = video['snippet']['thumbnails']['high']

                entries.append({
                    'video_id': video['snippet']['resourceId']['videoId'],
                    'video_title': video['snippet']['title'],
                    'video_url': f'https://www.youtube.com/watch?v={video["snippet"]["resourceId"]["videoId"]}',
                    'channel_title': video['snippet']['channelTitle'],
                    'url': f'https://www.youtube.com/channel/{video["snippet"]["channelId"]}',
                    'thumbnail': thumbnail,
                    'published_at': video['snippet']['publishedAt']
                })

        self.entries = entries

    def fetch_channel_data(self, channel_id: str):
        url = 'https://www.googleapis.com/youtube/v3/channels'

        params = {
            'key': self.api_key,
            'id': channel_id,
            'part': ['id', 'snippet', 'contentDetails']
        }

        channel_response = requests.get(url=url, params=params)

        if channel_response.status_code != 200:
            print(channel_response.status_code)
            print(channel_response.text)
            raise Exception('Unhandled status code while fetching channel data')

        return channel_response.json()

    def fetch_uploads(self, channel_data: dict):
        url = 'https://www.googleapis.com/youtube/v3/playlistItems'

        params = {
            'key': self.api_key,
            'playlistId': channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
            'part': ['snippet'],
            'maxResults': 15,
        }

        videos_response = requests.get(url=url, params=params)

        if videos_response.status_code != 200:
            print(videos_response.status_code)
            print(videos_response.text)
            raise Exception('Unhandled status code while fetching videos')

        return videos_response.json()['items']
