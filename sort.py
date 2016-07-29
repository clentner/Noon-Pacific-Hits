'''
Print a markdown table of the top tracks by YouTube view count.
'''
import json
import sys

def sorted_tracks(tracks):
    for i, track in enumerate(tracks):
        if 'listens' not in track:
            tracks[i]['listens'] = 0

    return sorted(tracks, key=lambda t: t['listens'], reverse = True)

def markdown_tracklist(top, npdata):
    mixtapes = {}
    for mix in npdata:
        mixtapes[mix['id']] = mix
        
    markdown = ('Views | Artist | Title | Playlist\n' +
                '----- | ------ | ----- | --------\n')
    for t in top:
        table_row = '[{:,}](https://youtube.com/watch?v={}) | {} | {} | [{}](http://beta.noonpacific.com/#/weekly/{}/{})'.format(
            t['listens'],
            t['video_id'],
            t['artist'],
            t['title'],
            mixtapes[t['mixtape']]['title'],
            mixtapes[t['mixtape']]['slug'],
            t['slug'])
        markdown += table_row + '\n'

    return markdown

def main():
    if len(sys.argv) > 1:
        num_tracks = int(sys.argv[1])
    else:
        num_tracks = 10

    with open('np-200-tracks.json', encoding='utf8') as f:
        tracks = json.load(f)
    with open('np-200.json', encoding='utf8') as f:
        npdata = json.load(f) # list of dicts containing lists of dicts

    st = sorted_tracks(tracks)[:num_tracks]
    print(markdown_tracklist(st, npdata))

if __name__ == '__main__':
    main()