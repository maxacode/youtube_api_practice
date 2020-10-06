# Program that interacts with Youtube API

# importing OS to get ENV vars
import os
# importing Google build module
from googleapiclient.discovery import build

# API key from ENV Var
api_key = os.environ.get('yt_api_key1')

# Building YT API
service = build('youtube', 'v3', developerKey=api_key)

#Asking user if they wanna use youtube ID or username:
userChoice = int(input("Would you like to use the Channel ID (1) or Username (2): "))
channelIdent = input("Enter the channel identifier based on above choice: ")
showwhat = int(input("What would you like to see: 1.Raw 2.View Count 3.Video Count 4. SubscriberCount 5.All of the Above: "))

#Based on usechoice this request will run.
if userChoice == 1:
    # Requesting YT info
    request = service.channels().list(
        part='statistics',
        id=channelIdent
    )
elif userChoice == 2:
    request = service.channels().list(
        part='statistics',
        forUsername=channelIdent
    )

#Executing the request.
response = request.execute()
#print(response)
viewCount = response['items'][0]['statistics']['viewCount']
viewCount = "This is the View Count:" + viewCount
videoCount = "This is the Video Count:" + response['items'][0]['statistics']['videoCount']
subscriberCount = "This is the Subscriber Count:" + response['items'][0]['statistics']['subscriberCount']

#Printing what the user requested.
if showwhat == 1:
    print("--------------------------------------------")
    print("THis is the full request: \n")
    print(response)
elif showwhat == 2:
    print("--------------------------------------------")
    print(viewCount)
elif showwhat == 3:
    print("--------------------------------------------")
    print(videoCount)
elif showwhat == 4:
    print("--------------------------------------------")
    print(subscriberCount)
elif showwhat == 5:
    print("--------------------------------------------")
    print("THis is the full request: \n")
    print(response)
    print("--------------------------------------------")
    print(viewCount)
    print("--------------------------------------------")
    print(videoCount)
    print("--------------------------------------------")
    print(subscriberCount)
else:
    print("--------------------------------------------")
    print("Somethign went wrong")
