import praw
import json



def create_reddit_obj(json_file="reddit_config.json", json_key="reddit_user_values"):
    with open(json_file) as f:
        data = json.load(f)

        user = data[json_key]
        reddit = praw.Reddit(client_id=user['client_id'],
                             client_secret=user['client_secret'],
                             user_agent=user['user_agent'],
                             username=user['username'],
                             password=user['password'])
        return reddit


reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

subred = reddit.subreddit("learnprogramming")

top = subred.top(limit=15)

file1 = open("topReddit.txt","w")
for i in top:
    if i.ups > 500:
        file1.write(i.title + "\n" + i.url + "\n")
        file1.write("\n")

file1.close()







