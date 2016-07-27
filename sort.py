'''
Print a markdown table of the top tracks by YouTube view count.
'''
import json

with open('np-200-tracks.json', encoding='utf8') as f:
    tracks = json.load(f)
with open('mixtape-titles.json', encoding='utf8') as f:
    titles = json.load(f)

for i, track in enumerate(tracks):
    if 'listens' not in track:
        tracks[i]['listens'] = 0

sorted_tracks = sorted(tracks, key=lambda t: t['listens'], reverse = True)
top = sorted_tracks[:10]
print('Views | Artist | Title | Playlist\n' +
      '----- | ------ | ----- | --------')
for t in top:
    print('{} | {} | {} | [{}](http://noonpacific.com/#/mix/{})'.format(
                                t['listens'],
                                t['artist'],
                                t['title'],
                                titles[str(t['mixtape'])],
                                t['mixtape']))