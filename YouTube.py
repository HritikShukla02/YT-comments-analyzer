from dotenv import load_dotenv
from request_retry import comments_request
import os
import requests
import pandas as pd
load_dotenv()

RAPID = os.getenv('RAPID_API_KEY')

def get_video_id(link):     
    try:
        video_id = link.split("=")[1].split('&')[0]
    except:
        video_id = link.split("/")[-1]
    return video_id


def get_comments(vid_id):
    comments = []
    authors = []
    author_ids = []
    comment_ids = []
    like_counts = []
    reply_count = []

    response = comments_request(vid_id=vid_id)
    continuation =True
    while continuation:
        data = response['data']
        for com in data:
            if "K" in com['likesCount']:
                likes = float(com['likesCount'].split("K")[0]) * 1000
            else:
                likes = int(com['likesCount'])

            if "K" in com['replyCount']:
                replies = float(com['replyCount'].split("K")[0]) * 1000
            else:
                replies = int(com['replyCount'])

            comments.append(com['textDisplay'])
            authors.append(com['authorText'])
            comment_ids.append(com['commentId'])
            author_ids.append(com['authorChannelId'])
            like_counts.append(likes)
            reply_count.append(replies)

        if response['continuation'] != "":
            token = response['continuation']
            response = comments_request(vid_id=vid_id, cont=token)
        else:
            continuation = False
        

    data = pd.DataFrame(data={
        "comment_id": comment_ids,
        "author_id": author_ids, 
        "author_name": authors,
        "comment": comments,
        "likes": like_counts,
        "replies": reply_count
    })
    return data