#Program that interacts with Youtube API

#importing OS to get ENV vars
import os

#importing Google build module
from googleapiclient.discovery import build

#API key from ENV Var
api_key = os.environ.get('yt_api_key1')
api_key = 'AIzaSyBviim_m_-23li4pBbqGKRC1B8jxXahVo0'

#Building YT API
service = build('youtube', 'v3', developerKey=api_key)

#Requesting YT info
request = service.channels().list(
    part='statistics',
    id='UCV4mvbLN6X1DBNcP9jY952g'
)

response = request.execute()

#print(response)

print("You have this many views: {}".format(response['items'][0]['statistics']['viewCount']))
