from collections import defaultdict
import pytest

from elephant_news.analysis import claims
from elephant_news.reddit import api
from elephant_news.tests.analysis.examples.article_1 import article, article_text
from elephant_news.utils.health_check import get_rich_print, save_test_log


@pytest.mark.reddit
def test_reddit_claim_check():
    article_claims = claims.list_claims(article_text)
    submissions = api.get_submissions_matching_url(article.url, 2)
    # api.check_submissions_relevance(submissions, title, url)
    all_claim_checks = []
    for submission in submissions:
        comments = api.get_submission_comments(submission)
        claim_checks = api.use_comments_to_check_claims(comments, article_claims)
        all_claim_checks.extend(claim_checks)
    dict_claim_checks = defaultdict(list)
    for claim_checks in all_claim_checks:
        dict_claim_checks[claim_checks.claim_id].append(claim_checks.objections)
    log_info = (
        ">>> We perform an end-to-end analysis on an article.\n\n" +
        ">>> Article text:\n" +
        get_rich_print(article_text) + "\n" +
        ">>> Claims:\n" +
        get_rich_print(article_claims) + "\n" +
        ">>> Analysis:\n" +
        get_rich_print(dict_claim_checks)
    )
    save_test_log('test_reddit_claim_check', log_info)
