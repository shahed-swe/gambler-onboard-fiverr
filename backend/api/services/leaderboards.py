import abc
import traceback

import pytz
import requests
from json import JSONDecodeError
from typing import Optional

from django.apps import apps
from django.utils import timezone


class Leaderboard(abc.ABC):
    leaderboard_id: str = None
    entries: Optional[list] = None
    updated_at: timezone.datetime = None

    def __init__(self, leaderboard_id):
        self.leaderboard_id = leaderboard_id

    def load(self):
        self.entries = []

    def fetch_data(self):
        pass

    @property
    def config(self):
        return apps.get_app_config('api').app_config['leaderboard'][self.leaderboard_id]

    @property
    def start_at(self) -> timezone.datetime:
        start_time = timezone.datetime.strptime(self.config['start_at'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.timezone('America/Chicago'))
        duration = self.config['duration_days']
        end_time = start_time + timezone.timedelta(days=duration)
        now = timezone.now()

        if now > end_time:
            days_passed_end = (now - end_time).days
            cycles_passed = days_passed_end // duration
            start_time = start_time + timezone.timedelta(days=(cycles_passed + 1) * duration)

        return start_time

    @property
    def end_at(self) -> timezone.datetime:
        duration = self.config['duration_days']
        return self.start_at + timezone.timedelta(days=duration)

    @property
    def prizes(self):
        return self.config['prizes']

    @property
    def sort_field(self) -> str:
        raise Exception('Not implemented')


class RoobetLeaderboard(Leaderboard):
    def fetch_data(self):
        entries = []

        try:
            url = self.config['api_endpoint']

            params = {
                'userId': '4fd215ba-67ad-4d41-909c-62b9469f5dd9',
                'startDate': self.start_at.isoformat(),
                'endDate': self.end_at.isoformat()
            }

            headers = {
                'Authorization': 'Bearer ' + self.config['api_key']
            }

            response = requests.get(url=url, params=params, headers=headers)
            print(response.text)
            if response.status_code == 200:
                entries = response.json()
                entries = sorted(entries, key=lambda x: x['wagered'], reverse=True)
                entries = entries[0:min(len(entries), 10)]

                for index, entry in enumerate(entries):
                    entry['name'] = entry['username']
                    entry['wagered'] = 0 if entry['wagered'] <= 0 else round(entry['wagered'])
                    entry['position'] = index + 1
                    entry['prize'] = 0.0 if index >= len(self.prizes) else self.prizes[index]
            else:
                print(response.json())
                raise Exception('Unhandled status code')
        except JSONDecodeError:
            print('Failed to fetch leaderboard data from Roobet')
        except Exception:
            print('Failed to fetch leaderboard data from Roobet')
            print(traceback.format_exc())

        self.entries = entries
        self.updated_at = timezone.now()

    @property
    def sort_field(self) -> str:
        return 'wagered'
