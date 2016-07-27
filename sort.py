'''
Print a markdown table of the top tracks.
'''

import json

with open('np-200-tracks.json', encoding='utf8') as f:
    tracks = json.load(f)

for i, track in enumerate(tracks):
    if 'listens' in track:
        tracks[i]['listens'] = int(track['listens'])
    else:
        tracks[i]['listens'] = 0

sorted_tracks = sorted(tracks, key=lambda t: t['listens'], reverse = True)
top = sorted_tracks[:10]
top_pretty = ['{} | {} | {}'.format(t['listens'], t['artist'], t['title'])
                for t in top]
print('Views | Artist | Title \n' +
      '----- | ------ | -----')
for s in top_pretty:
    print(s)