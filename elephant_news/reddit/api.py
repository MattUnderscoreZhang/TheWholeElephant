from dotenv import load_dotenv
import os
import praw
from praw.reddit import Submission


load_dotenv()  # .env file
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")


reddit = praw.Reddit(
    client_id="tGdEB115KZpDj1rOdDdNYQ",
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="macos:com.example.the_whole_elephant:0.0.1 (by /u/whatisthis_whereami)",
)


def get_hot_threads_from_subreddit(subreddit_name: str, n_threads: int | None = None) -> list[Submission]:
    subreddit = reddit.subreddit(subreddit_name)
    threads = subreddit.hot(limit=n_threads)
    return [thread for thread in threads]


def get_threads_matching_url(url: str, n_threads: int | None = None) -> list[Submission]:
    subreddit = reddit.subreddit("all")
    threads = subreddit.search(f"url: \"{url}\"", limit=n_threads)
    return [thread for thread in threads]
