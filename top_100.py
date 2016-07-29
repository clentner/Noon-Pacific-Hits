import json

import top

with open('np-200-tracks.json', encoding='utf8') as f:
    tracks = json.load(f)
with open('np-200.json', encoding='utf8') as f:
    npdata = json.load(f) # list of dicts containing lists of dicts

st = top.sorted_tracks(tracks)[:100]
contents = top.markdown_tracklist(st, npdata, True)
with open('top_100.md', 'w', encoding='utf8') as target:
    target.write(contents)