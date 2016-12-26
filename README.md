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

Views | Artist | Title | Hipsterness | Playlist
----- | ------ | ----- | ----------- | --------
[689,153,621](https://youtube.com/watch?v=pB-5XG-DbAA) | Sam Smith | Stay With Me | 3 days after YouTube release | [NOON // 080](http://noonpacific.com/#/weekly/noon-080/sam-smith-stay-with-me)
[669,193,626](https://youtube.com/watch?v=jGflUbPQfW8) | OMI (Felix Jaehn remix) | Cheerleader | 93 days before YouTube release | [NOON // 120](http://noonpacific.com/#/weekly/noon-120/omi-felix-jaehn-remix-cheerleader)
[423,652,045](https://youtube.com/watch?v=tD4HCZe-tew) | LA+CH | Hi-Life | 247 days before YouTube release | [NOON // 110](http://noonpacific.com/#/weekly/noon-110/la-ch-hi-life)
[384,760,028](https://youtube.com/watch?v=9Sc-ir2UwGU) | Kygo feat. Conrad | Firestone | 91 days before YouTube release | [NOON // 116](http://noonpacific.com/#/weekly/noon-116/kygo-feat-conrad-firestone)
[362,597,189](https://youtube.com/watch?v=MYSVMgRr6pw) | Hozier | Take Me To Church | 19 days after YouTube release | [NOON // 057](http://noonpacific.com/#/weekly/noon-057/hozier-take-me-to-church)
[285,173,318](https://youtube.com/watch?v=iX-QaNzd-0Y) | Milky Chance | Stolen Dance | 53 days after YouTube release | [NOON // 037](http://noonpacific.com/#/weekly/noon-037/milky-chance-stolen-dance)
[267,886,817](https://youtube.com/watch?v=5NV6Rdv1a3I) | Daft Punk feat. Pharrell | Get Lucky | 4 days before YouTube release | [NOON // 032](http://noonpacific.com/#/weekly/noon-032/daft-punk-feat-pharrell-get-lucky)
[217,088,879](https://youtube.com/watch?v=KDxJlW6cxRk) | Duke Dumont | Ocean Drive | 43 days before YouTube release | [NOON // 150](http://noonpacific.com/#/weekly/noon-150/duke-dumont-ocean-drive)
[202,308,478](https://youtube.com/watch?v=FHCYHldJi_g) | Duke Dumont feat. Jax Jones | I Got U | 37 days before YouTube release | [NOON // 069](http://noonpacific.com/#/weekly/noon-069/duke-dumont-feat-jax-jones-i-got-u)
[176,056,939](https://youtube.com/watch?v=BS46C2z5lVE) | Route 94 | My Love | 77 days after YouTube release | [NOON // 082](http://noonpacific.com/#/weekly/noon-082/route-94-my-love)


[Click here for the top 100 list.](top_100.md)


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