import typing
import sqlite3
import requests

from twitch_user_logger.api.database import user_exists, insert_user


class Twitch:
    def __init__(self, client_id: str, client_secret: str, db: sqlite3.Connection = None):
        self.oauth = self._get_token(client_id, client_secret)
        self.access_token = self.oauth.get('access_token')

        if self.access_token:
            self.headers = {
                'client-id': client_id,
                'Authorization': f'Bearer {self.access_token}'
            }

    def _get_token(self, client_id, client_secret) -> typing.Dict:
        resp = requests.post(
            'https://id.twitch.tv/oauth2/token',
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': 'client_credentials'
            }
        )

        if resp.status_code != 200:
            raise Exception(resp.content)

        return resp.json()
    
    def get_user(self, user_id: str) -> typing.Dict:
        requests.get(
            "https://api.twitch.tv/helix/users",
            params={
                'id': user_id
            },
            headers=self.headers
        )

        if resp.status_code != 200:
            raise Exception(resp.content)

        return resp.json()

    def get_users(self, user_ids: typing.List[str] = None) -> typing.Dict:
        if len(user_ids) > 100:
            raise Exception('No more than 100 users allowed at a time.')

        requests.get(
            "https://api.twitch.tv/helix/users",
            params={
                'id': user_ids
            },
            headers=self.headers
        )

        if resp.status_code != 200:
            raise Exception(resp.content)

        return resp.json()

    def crawl_streams(self, after: str = None) -> typing.Dict:
        data = {
            'first': 100
        }

        if after:
            data['after'] = after

        resp = requests.get(
            "https://api.twitch.tv/helix/streams",
            params=data,
            headers=self.headers
        )

        if resp.status_code != 200:
            raise Exception(resp.content)

        return resp.json()

    def handle_user(self, user: typing.Dict) -> None:
        if not user_exists(user.id):
            insert_user(user)
