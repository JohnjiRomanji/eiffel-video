import praw
import requests
import io
from PIL import Image
import csv
import datetime


# Reddit API credentials
reddit = praw.Reddit(
    client_id="cZNXru_AwPjqoACb8-Qhxg",
    client_secret="Uh1dYyx7E8fSiafBSFo0StdUr6Lkmw",
    user_agent="script:com.example.eiffel:v0.0.1 (by u/NormalProfessional)"
)

subs=["pics", "all", "FrancePics", "photography"]
x=0
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"eiffel_posts_{now}.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Image URL", "Post Permalink", "Post URL"])

    for sub_str in subs:
        # Select subreddit and search for posts containing "Eiffel Tower"
        sub = reddit.subreddit(sub_str)
        posts = sub.search("Eiffel Tower", limit=1000)

        # Download images and process with Pillow
        for post in posts:
            if post.url.endswith(".jpg") or post.url.endswith(".png"):
                print(post.url)
                print(post.permalink)
                url = f"https://www.reddit.com{post.permalink}"
                print(url)
                writer.writerow([post.url, post.permalink, url])
                x+=1
    print(x)


