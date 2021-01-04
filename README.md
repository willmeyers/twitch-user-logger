# Twitch User Crawler

This project was built for the purpose of building a complete twitch partner user dataset.

## How it Works

We follow a simple algorithm:

1. Get all streams currently live (at the current cursor position)
2. Iterate over all streams
3. When we encounter a unique Twitch user id, get that user's info
4. If the user is a partner, we add it to the database

Since the chance we'll catch a partner's stream is random, we increase the chances by 
setting the `crawl_period` (the number of days to look for partners) to a period of serveral 
days. Because partners stream fairly regularly in order to maintain consistent viewership, 
anywhere from 7 to 30 days should be sufficient. 

## Refreshing Access Token?

While you can make edits to the underlying logic, Twitch expires access
tokens (as if Jan. 2021) in about 50 days. Plenty of time for the crawler
to do its thing.

## Downloads

*We are currently running the crawler! Check back soon*

## License

The crawler is licensed under MIT. The dataset is completely free (consider it under Create 
Commons).

### Shoutouts

This project was inspired by ...

The data provided can be used in conjunction with data from ... to create a more in-depth 
analysis.
