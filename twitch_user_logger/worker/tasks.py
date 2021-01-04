import datetime

from twitch_user_logger.api.twitch import Twitch


def get_streams(crawl_period: int = 7, crawl_wait: int = 30) -> None:
    end_time = datetime.datetime.now() + datetime.timedelta(days=7)

    t = Twitch()

    streams = t.crawl_streams()

    try:
        cursor = streams['pagination']['cursor']
    except KeyError:
        raise StopIteration('No cursor')

    while True:
        if datetime.datetime.now() >= end_time:
            raise StopIteration('Reached end time.')

        try:
            streams = t.crawl_streams(after=cursor)

            steamer_set = set()

            for stream in streams['data']:
                streamer_id = steam['user_id']
                steamer_set.add(streamer_id)

            if steamer_set:
                users = t.get_users(steamer_set)

                for user in users:
                    t.handle_user(user):

            try:
                cursor = streams['pagination']['cursor']
            except KeyError:
                raise StopIteration('No cursor')

        except Exception:
            break

        except StopIteration:
            break
