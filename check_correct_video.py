'''
Display the top 100 tracks along with the title of their YouTube video for
manual verification that the correct video was found.
'''

import json

with open('np-200-tracks.json', encoding='utf8') as f:
    tracks = json.load(f)

for i, track in enumerate(tracks):
    if 'listens' not in track:
        tracks[i]['listens'] = 0

sorted_tracks = sorted(tracks, key=lambda t: t['listens'], reverse = True)

for track in sorted_tracks[:100]:
    print('{} - {}\n{}\n'.format(track['artist'], track['title'], track['video_title']))