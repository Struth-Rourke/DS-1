import os
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

# HACKER_NEWS Credentials
HACKER_NEWS_API_KEY = os.getenv("HACKER_NEWS_API_KEY")
HACKER_NEWS_API_SECRET = os.getenv("HACKER_NEWS_API_SECRET")
HACKER_NEWS_ACCESS_TOKEN = os.getenv("HACKER_NEWS_ACCESS_TOKEN")
HACKER_NEWS_ACCESS_TOKEN_SECRET = os.getenv("HACKER_NEWS_ACCESS_TOKEN_SECRET")


# Authorization Information(.env) -- via Tweepy package
auth = tweepy.OAuthHandler(HACKER_NEWS_API_KEY, HACKER_NEWS_API_SECRET)
auth.set_access_token(HACKER_NEWS_ACCESS_TOKEN, HACKER_NEWS_ACCESS_TOKEN_SECRET)
print("AUTH:", auth)

# API via auth keys
api = tweepy.API(auth)
print("API:", api)
#print(dir(api))


# Wrapper Function
# def HACKER_NEWS_api():
#     auth = tweepy.OAuthHandler(HACKER_NEWS_API_KEY, HACKER_NEWS_API_SECRET)
#     auth.set_access_token(HACKER_NEWS_ACCESS_TOKEN, HACKER_NEWS_ACCESS_TOKEN_SECRET)
#     print("AUTH", auth)
#     api = tweepy.API(auth)
#     print("API", api)
#     #print(dir(api))
#     return api


if __name__ == "__main__":

    # TODO:
    # Getting tweets from a specified given user
    comments = api.user_timeline("rourke_robert_", 
                                 tweet_mode="extended", 
                                 count=150, 
                                 exclude_replies=True, 
                                 include_rts=False)
    
    # TODO:
    # For loop to retrieve all the tweets w/ full text
    for comment in comments:
        print("-----")
        print(comment.full_text)
