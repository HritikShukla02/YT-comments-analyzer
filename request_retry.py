from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

RAPID = os.getenv("RAPID_API_KEY")


def req_retry(url, params, headers={}):
    delay = 1
    backoff = 2
    retry_count = 3
    attempts = 0
    while attempts < retry_count:
        try:
        

            response = requests.get(url, params, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as ex:
            attempts += 1
            if attempts == retry_count:
                print('retry count exceeded for url: '+ url)
                raise ex
            
            time.sleep(delay)
            delay *= backoff


def comments_request(vid_id, cont=""):
    url = "https://yt-api.p.rapidapi.com/comments"

    querystring = {"id":vid_id}

    headers = {
        "x-rapidapi-key": "90038e520fmsh054eb12ecf7ca91p1f29eejsn73bf7ccfb53c",
        "x-rapidapi-host": "yt-api.p.rapidapi.com",
        "X-TOKEN": cont
    }

    response = req_retry(url=url, headers=headers, params=querystring)

    data = response.json()
    return data



        
