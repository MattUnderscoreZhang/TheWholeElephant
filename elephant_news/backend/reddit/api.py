from dataclasses import dataclass
from datetime import datetime
from dotenv import load_dotenv
import json
import os
import praw
from praw.reddit import Submission
import re

from elephant_news.analysis.claims import Claim
from elephant_news.llm.llm import llm_api
from elephant_news.llm.log import Log, Message


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
    log = Log("gpt-3.5-turbo")
    claims_text = "".join([f"{claim.id}: {claim.claim}" for claim in claims])
    parsed_comments = [re.sub('\n +', '\n', re.sub('\n', ' ', re.sub(' +', ' ', comment))) for comment in comments]
    comments_text = "\n".join(parsed_comments)
    query = f"""
A list of claims from an article are listed in triple quotes.
Some reaction comments are listed below that.
For each claim, summarize the objections to the claim made by the comments.
Format your response as a JSON list, with the following keys:
- claim_id (int): claim ID
- objections (str): a summary of objections

Claims: '''{claims_text}'''

Comments: '''{comments_text}'''
"""
    message = Message("user", query)
    log.add_message(message)
    response_text = llm_api(log)
    response = json.loads(response_text)
    response = [ClaimCheck(**claim_check) for claim_check in response]
    return response
