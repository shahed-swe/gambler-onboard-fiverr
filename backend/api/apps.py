import json
import sys

from django.apps import AppConfig

from backend.api.services.background import BackgroundProcessor
from backend.api.services.kick import Kick
from backend.api.services.leaderboards import RoobetLeaderboard, Leaderboard
from backend.api.services.youtube import YouTube


class ApiConfig(AppConfig):
    name: str = 'backend.api'
    loaded: bool = False
    app_config: dict = None
    background: BackgroundProcessor = None
    leaderboards: list[Leaderboard] = None
    youtube: YouTube = None
    kick: Kick = None

    def __init__(self, app_name, app_module):
        super(ApiConfig, self).__init__(app_name, app_module)

        self.loaded = False

    def ready(self):
        if 'manage.py' in sys.argv[0] and sys.argv[1] != 'runserver':
            print('Skip loading application...')
            return

        self.load_config()

        if not self.loaded:
            self.leaderboards = [
                RoobetLeaderboard('roobet'),
            ]

            for leaderboard in self.leaderboards:
                leaderboard.load()

            self.youtube = YouTube()
            self.youtube.load()

            self.kick = Kick()
            self.kick.load()

            self.background = BackgroundProcessor()
            self.background.init_on_new_thread()
            self.background.schedule_repeating_task(60, self.load_config)

            for leaderboard in self.leaderboards:
                self.background.schedule_repeating_task(60 * 5, leaderboard.fetch_data)

            self.background.schedule_repeating_task(60 * 5, self.youtube.fetch_data)
            # self.background.schedule_repeating_task(60 * 5, self.kick.fetch_data)

            self.loaded = True

            print('Backend services are running')

    def load_config(self):
        self.app_config = json.loads(open('./app.json', 'r').read())
