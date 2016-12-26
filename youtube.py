'''
Quick wrapper around the relevant parts of the YouTube API.
Provides methods for searching videos and retrieving statistics.

Methods will raise requests.exceptions.HTTPError on 4xx and 5xx
status codes. Methods that require a video id will raise IndexError
if it is bad (does not refer to a valid video).
'''

import json
import os
import requests
import urllib.parse

class YouTube():
    def __init__(self, api_key = None):
        if not api_key:
            api_key = os.environ.get('YOUTUBE-API-KEY')
        self.api_key = api_key
        self.search_endpoint = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={}&type=video&key=' + api_key
        self.statistics_endpoint = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={}&key=' + api_key
        self.snippet_endpoint = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={}&key=' + api_key
            
    def search_first(self, query):
        '''
        Search youtube for `query` and return the id and title of the first result
        Returns None on no video found.
        video_id = result['id']['videoId']
        video_title = result['snippet']['title']
        video_date = result['snippet']['publishedAt']
        '''
        search_url = self.search_endpoint.format(urllib.parse.quote_plus(query))
        r = requests.get(search_url)
        r.raise_for_status() # Raise exception on 4xx or 5xx status code
            
        search_result = r.json()
        if search_result['pageInfo']['totalResults'] < 1:
            return None
            
        return search_result['items'][0]
        
    def snippet(self, id):
        '''
        Retrieve the snippet of a video by its id (str).
        '''
        title_url = self.snippet_endpoint.format(id)
        r = requests.get(title_url)
        r.raise_for_status() # Raise exception on 4xx or 5xx status code
        
        response = r.json()
        return response

    def view_count(self, id):
        '''
        Retrieve the view count of a video by its id (str).
        Raises IndexError on nonexistent video.
        '''
        statistics_url = self.statistics_endpoint.format(id)
        r = requests.get(statistics_url)
        r.raise_for_status() # Raise exception on 4xx or 5xx status code
        
        statistics = r.json()
        return int(statistics['items'][0]['statistics']['viewCount'])

