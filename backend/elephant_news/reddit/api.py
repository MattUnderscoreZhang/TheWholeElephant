from dataclasses import dataclass
from dotenv import load_dotenv
import json
import os
import praw
from praw.reddit import Submission
import re

from elephant_news.analysis.claims import Claim
from elephant_news.llm.llm import Log
from elephant_news.utils.text_parsing import batch_strings_into_max_encoding_length_batches


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


def use_comments_to_check_claims(comments: list[str], claims: list[Claim], model: str = "gpt-3.5-turbo-16k") -> list[ClaimCheck]:
    log = Log(model)
    claims_text = "\n".join([f"{claim.id}: {claim.claim}" for claim in claims])
    query = f"""
A list of claims from an article are listed in triple quotes.
Some reaction comments are listed below that.
For each claim, summarize the objections to the claim made by the comments.
Format your response as a JSON list, with the following keys:
- claim_id (int): claim ID
- objections (str): a summary of objections

Claims: '''\n{claims_text}\n'''
"""
    query_encoding_length = log.get_encoding_length(query)
    max_comment_batch_encoding_length = log.get_model_max_encoding_length() - query_encoding_length - log.get_encoding_length("\nComments: '''\n'''")
    max_comment_batch_encoding_length -= len(claims) * 100  # response length

    parsed_comments = [re.sub('\n +', '\n', re.sub('\n', ' ', re.sub(' +', ' ', comment))) for comment in comments]
    encoding_lengths = [log.get_encoding_length(comment + '\n') for comment in parsed_comments]
    comment_batches = batch_strings_into_max_encoding_length_batches(
        strings=parsed_comments,
        string_encoding_lengths=encoding_lengths,
        max_encoding_length=max_comment_batch_encoding_length,
    )

    claim_checks = []
    for comment_batch in comment_batches:
        query_and_comments = query + f"\nComments: '''\n{comment_batch}'''"
        response_text = log.ask(query_and_comments)
        try:
            response = json.loads(response_text)
            claim_checks += [ClaimCheck(**claim_check) for claim_check in response]
        except:
            # TODO: handle this case
            breakpoint()
    return claim_checks
