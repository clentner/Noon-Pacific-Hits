'''
Takes the full Noon Pacific index in json format (e.g. np-200.json) and
adds YouTube plays to each track that has a corresponding YouTube video.
Outputs the resulting information as a combined JSON array.
Analysis should be performed on the output file, not as part of this
script. This will be faster and less burdensome on the api quota.
'''

import json
import requests.exceptions
from youtube import YouTube

def main():
    # The main Noon Pacific index
    npfile = 'np-200.json'
    # List of ids of tracks for which no corresponding video exists
    no_video_file = 'no-youtube-video.json'
    # Dictionary mapping ids to correct video results
    wrong_video_file = 'wrong-youtube-video.json'
    
    with open(npfile, encoding='utf8') as f:
        npdata = json.load(f) # list of dicts containing lists of dicts
    with open(no_video_file) as f:
        no_video = set(json.load(f))
    with open(wrong_video_file) as f:
        corrected_video_id = json.load(f)

    # Aggregate all the tracks into one list
    tracks = []
    for mixtape in npdata:
        tape_tracks = mixtape['tracks']
        for track in tape_tracks:
            track['np_release'] = mixtape['release']
        tracks.extend(tape_tracks)

    # Add youtube plays to each track's data
    yt = YouTube()
    for i, track in enumerate(tracks):
        try:
            if track['id'] in no_video:
                # There is no youtube video for this track.
                continue
            if track['id'] in corrected_video_id:
                video_id = corrected_video_id[track['id']]
                snippet = yt.snippet(video_id)
                s = snippet['items'][0]['snippet']
            else:
                q = track['artist'] + ' ' + track['title']
                result = yt.search_first(q)
                if not result:  # No video found
                    continue
                s = result['snippet']
                video_id = result['id']['videoId']

            video_title = s['title']
            video_date = s['publishedAt']

            video_view_count = yt.view_count(video_id)
            
            # Add the new data to the track
            tracks[i].update({'video_id': video_id,
                              'video_title': video_title,
                              'video_date': video_date,
                              'listens': video_view_count})
            print(video_title) # Just for progress monitoring
                              
        except requests.exceptions.HTTPError as e:
            # A server-side error from the API
            # Just eat these errors if they occur. There are too many
            # songs to analyze to worry about one missing track.
            print(str(e))
            continue
            
    # Write out the new extended track data
    with open('np-200-tracks.json', 'w', encoding='utf8') as f:
        json.dump(tracks, f, indent=4)

if __name__ == '__main__':
    main()
