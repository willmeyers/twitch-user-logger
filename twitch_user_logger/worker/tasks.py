from twitch_user_logger.api.twitch import Twitch


def get_streams():
    t = Twitch()

    streams = t.crawl_streams()

    try:
        cursor = streams['pagination']['cursor']
    except KeyError:
        raise StopIteration('No cursor')

    while True:
        try:
            streams = t.crawl_streams(after=cursor)

            try:
                cursor = streams['pagination']['cursor']
            except KeyError:
                raise StopIteration('No cursor')
                
        except StopIteration:
            break