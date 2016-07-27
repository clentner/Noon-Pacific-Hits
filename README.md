Noon Pacific Hits
=================

Intro
-----
[Noon Pacific](https://noonpacific.com/) is a weekly music playlist that
has been releasing new playlists since September 2012. Along the way, it
has helped popularize obscure artists, collaborated with nonprofits, hosted
AMAs with featured artists, and gotten ahead of some of the biggest hits of
all time.

Remember Hozier's "Take Me To Church"? Noon Pacific featured that track
within days of its release. What about Daft Punk's "Get Lucky"?

In anticipation of Noon Pacific's four year anniversary, this project aims
to collect statistics about the playlist service's history. What were the
biggest hits discovered before their prime? What artists have made the most
repeat appearances?


Results
-------
The top 10 songs to have appeared on Noon Pacific, ordered by YouTube view
counts, are:

Views | Artist | Title | Playlist
----- | ------ | ----- | --------
639024884 | Sam Smith | Stay With Me | [NOON // 080](http://noonpacific.com/#/mix/158)
586249598 | OMI (Felix Jaehn remix) | Cheerleader | [NOON // 120](http://noonpacific.com/#/mix/132)
341701291 | Hozier | Take Me To Church | [NOON // 057](http://noonpacific.com/#/mix/120)
306927123 | Kygo feat. Conrad | Firestone | [NOON // 116](http://noonpacific.com/#/mix/144)
258224025 | Milky Chance | Stolen Dance | [NOON // 037](http://noonpacific.com/#/mix/91)
179808881 | Duke Dumont feat. Jax Jones | I Got U | [NOON // 069](http://noonpacific.com/#/mix/143)
152729868 | Route 94 | My Love | [NOON // 082](http://noonpacific.com/#/mix/160)
152591564 | Duke Dumont | Ocean Drive | [NOON // 150](http://noonpacific.com/#/mix/214)
143373570 | Klingande | Jubel | [NOON // 039](http://noonpacific.com/#/mix/93)
136160266 | Daft Punk feat. Pharrell | Get Lucky | [NOON // 032](http://noonpacific.com/#/mix/86)


The artists with the most appearances on Noon Pacific are:

Appearances | Artist
----------- | ------
10 | HONNE
6 | Wildcat! Wildcat!
6 | Roosevelt
6 | Leo Kalyan
6 | Chet Faker
6 | Jungle
6 | Beat Connection


Usage
-----
* You can use the pre-generated np-200-tracks.json file, or:
* You will need a [YouTube API key](https://developers.google.com/youtube/v3/getting-started).
Note: This program will use about 200K of your 1M daily quota.
* Set the environment variable YOUTUBE-API-KEY to the key
you have obtained.
* Run `add_youtube_data.py` to get updated view counts for each song.
Note: Due to poor Windows console support of Unicode, you will either
need to run in a different console, redirect output to a file, or install
[win_unicode_console](https://pypi.python.org/pypi/win_unicode_console)
on Windows.
* Analyze the resulting json file.

Caveats
-------
YouTube Search isn't magic, so sometimes it comes up with a video that
does not correspond to the track in question. Also, some of the tracks
do not have YouTube videos at all.

To combat these problems, hand-edited supplementary files are used. These
files are incomplete.
* `no-youtube-video.json` is a list of ids, corresponding to tracks in
the index for which no video is available.
* `wrong-youtube-video.json` is a dictionary mapping ids to their correct
YouTube id, for instances in which search returns the wrong video.