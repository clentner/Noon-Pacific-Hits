'''
List artists by number of appearances on Noon Pacific.
'''
import collections
import json

with open('np-200-tracks.json', encoding='utf8') as f:
    tracks = json.load(f)

artists = (track['artist'] for track in tracks)
counted = collections.Counter(artists)
top = counted.most_common(20)

print('Appearances | Artist\n' +
      '----------- | ------')
for (artist, count) in top:
    print('{} | {}'.format(count, artist))
