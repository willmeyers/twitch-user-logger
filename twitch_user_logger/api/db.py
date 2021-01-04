import typing
from datetime import datetime


class User:
    id: str
    broadcaster_type: str
    description: str
    display_name: str
    email: str
    login: str
    offline_image_url: str
    profile_image_url: str
    type: str
    view_count: str
    created_at: str


def _setup_database(name: str) -> str:
    pass


def _export_database(format: str , release: str, crawl_period: typing.Tuple[datetime, datetime]) -> str:
    pass


def 