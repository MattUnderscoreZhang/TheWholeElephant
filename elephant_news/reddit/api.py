from dataclasses import dataclass
from datetime import datetime
from dotenv import load_dotenv
import os
import praw
from praw.reddit import Submission

from elephant_news.analysis.claims import Claim


load_dotenv()  # .env file
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")


reddit = praw.Reddit(
    client_id="tGdEB115KZpDj1rOdDdNYQ",
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="macos:com.example.the_whole_elephant:0.0.1 (by /u/whatisthis_whereami)",
)


def get_hot_submissions_from_subreddit(subreddit_name: str, n_submissions: int | None = None) -> list[Submission]:
    subreddit = reddit.subreddit(subreddit_name)
    submissions = subreddit.hot(limit=n_submissions)
    return [submission for submission in submissions]


def get_submissions_matching_url(url: str, n_submissions: int | None = None) -> list[Submission]:
    subreddit = reddit.subreddit("all")
    submissions = subreddit.search(f"url: \"{url}\"", limit=n_submissions)
    return [submission for submission in submissions]


def get_submissions_matching_title(title: str, n_submissions: int | None = None) -> list[Submission]:
    subreddit = reddit.subreddit("all")
    submissions = subreddit.search(f"{title}", limit=n_submissions)
    return [submission for submission in submissions]


def check_submissions_relevance(submissions: list[Submission], title: str, url: str) -> float:
    """
    submission.title
    submission.subreddit.display_name
    str(datetime.fromtimestamp(submission.created_utc))
    submission.url
    submission.comments
    """
    raise NotImplementedError


def get_submission_comments(submission: Submission) -> list[str]:
    submission.comments.replace_more(limit=None)
    return [comment.body for comment in submission.comments.list()]


@dataclass
class ClaimCheck:
    claim_id: int
    objections: list[str]


def use_comments_to_check_claims(comments: list[str], claims: list[Claim]) -> list[ClaimCheck]:
    raise NotImplementedError
