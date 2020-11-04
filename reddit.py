import praw
import random
import requests


reddit = praw.Reddit(client_id='YOUR CLIENT ID',client_secret='YOUR CLIENT SECRET',
                         user_agent='USER AGENT')
urls = []
subreddit = reddit.subreddit("memes")  #You can change it to any subreddit.
for submission in subreddit.hot(limit=50):
        urls.append((submission.url)) #To list top 50 meme's url

try :
    random_selector = random.randint(0, 50)
    random_url = urls[random_selector]
    response = requests.get(random_url)
    file = open("memes/post.png", "wb") #Directory settings
    file.write(response.content)
    print("MEME IS DOWNLOADED SUCCESSFULLY")

except:
    print("Something went wrong.")


























