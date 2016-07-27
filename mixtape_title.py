'''
Creates a mapping between internal mixtape ids (which are monotonic but not sequential) and their titles
(which include more normal numberings).
'''
import json

with open('np-200.json', encoding='utf8') as f:
    npdata = json.load(f) # list of dicts containing lists of dicts

mapping = {}
for mix in npdata:
    mapping[str(mix['id'])] = mix['title']
    
with open('mixtape-titles.json', 'w', encoding='utf8') as f:
    json.dump(mapping, f, indent=4)