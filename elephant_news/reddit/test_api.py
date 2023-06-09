from dotenv import load_dotenv
import os
import praw
from praw.reddit import Submission


load_dotenv()  # .env file
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")


reddit = praw.Reddit(
    client_id="tGdEB115KZpDj1rOdDdNYQ",
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="The Whole Elephant",
)


def get_threads(subreddit_name: str, n_threads: int) -> list[Submission]:
    subreddit = reddit.subreddit(subreddit_name)
    threads = subreddit.hot(limit=n_threads)
    return [thread for thread in threads]


def test_api():
    threads = get_threads("wallstreetbets", 10)
    for thread in threads:
        print(thread.title)
