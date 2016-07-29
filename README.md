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
[639,024,884](https://youtube.com/watch?v=pB-5XG-DbAA) | Sam Smith | Stay With Me | [NOON // 080](http://beta.noonpacific.com/#/weekly/noon-080/sam-smith-stay-with-me)
[586,249,598](https://youtube.com/watch?v=jGflUbPQfW8) | OMI (Felix Jaehn remix) | Cheerleader | [NOON // 120](http://beta.noonpacific.com/#/weekly/noon-120/omi-felix-jaehn-remix-cheerleader)
[341,701,291](https://youtube.com/watch?v=MYSVMgRr6pw) | Hozier | Take Me To Church | [NOON // 057](http://beta.noonpacific.com/#/weekly/noon-057/hozier-take-me-to-church)
[306,927,123](https://youtube.com/watch?v=9Sc-ir2UwGU) | Kygo feat. Conrad | Firestone | [NOON // 116](http://beta.noonpacific.com/#/weekly/noon-116/kygo-feat-conrad-firestone)
[258,224,025](https://youtube.com/watch?v=iX-QaNzd-0Y) | Milky Chance | Stolen Dance | [NOON // 037](http://beta.noonpacific.com/#/weekly/noon-037/milky-chance-stolen-dance)
[179,808,881](https://youtube.com/watch?v=FHCYHldJi_g) | Duke Dumont feat. Jax Jones | I Got U | [NOON // 069](http://beta.noonpacific.com/#/weekly/noon-069/duke-dumont-feat-jax-jones-i-got-u)
[152,729,868](https://youtube.com/watch?v=BS46C2z5lVE) | Route 94 | My Love | [NOON // 082](http://beta.noonpacific.com/#/weekly/noon-082/route-94-my-love)
[152,591,564](https://youtube.com/watch?v=KDxJlW6cxRk) | Duke Dumont | Ocean Drive | [NOON // 150](http://beta.noonpacific.com/#/weekly/noon-150/duke-dumont-ocean-drive)
[143,373,570](https://youtube.com/watch?v=b6vSf0cA9qY) | Klingande | Jubel | [NOON // 039](http://beta.noonpacific.com/#/weekly/noon-039/klingande-jubel)
[136,160,266](https://youtube.com/watch?v=h5EofwRzit0) | Daft Punk feat. Pharrell | Get Lucky | [NOON // 032](http://beta.noonpacific.com/#/weekly/noon-032/daft-punk-feat-pharrell-get-lucky)


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