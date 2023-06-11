from praw.reddit import Submission
import pytest

from elephant_news.analysis.claims import Claim
from elephant_news.reddit import api


def test_get_hot_submissions_from_subreddit():
    submissions = api.get_hot_submissions_from_subreddit("wallstreetbets", 10)
    titles = [submission.title for submission in submissions]
    assert len(titles) == 10
    assert all([type(title) == str for title in titles])


def test_get_submissions_matching_url():
    url = "https://www.cnn.com/2023/05/21/us/naacp-florida-travel-advisory/index.html"
    submissions = api.get_submissions_matching_url(url, 10)
    titles = [submission.title for submission in submissions]
    assert titles == [
        'NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under Gov. DeSantis’ administration',
        "NAACP issues travel advisory for Florida, saying the state is 'openly hostile toward African Americans' under Gov. DeSantis' administration | CNN",
        'NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under DeSantis due to the recent bans on Critical Race Theory in classrooms. According to Florida’s Department of Education, CRT “significantly lacks educational value.”',
        'NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under Gov. DeSantis’ administration',
        'As someone who recently stays in Florida, I think they might have this backwards.... 🤣',
        "NAACP issues travel advisory for Florida, saying the state is 'openly hostile toward African Americans' under Gov. DeSantis' administration | CNN",
    ]


def test_get_submissions_matching_title():
    title = "NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under Gov. DeSantis’ administration"
    submissions = api.get_submissions_matching_title(title, 10)
    titles = [submission.title for submission in submissions]
    assert "NAACP issues travel advisory for Florida, saying the state is 'openly hostile toward African Americans' under Gov. DeSantis' administration" in titles


@pytest.mark.reddit
def test_check_submissions_relevance():
    submissions = [
        next(api.reddit.subreddit("politics").search(f"url: https://www.cnn.com/2023/05/21/us/naacp-florida-travel-advisory/index.html", limit=1)),
        next(api.reddit.subreddit("BlackPeopleTwitter").search(f"Bernice King responds to Ted Cruz condemning NAACP for Florida travel advisory", limit=1)),
        next(api.reddit.subreddit("BlackPeopleTwitter").search(f"NAACP issues Florida Travel Advisory", limit=1)),
        next(api.reddit.subreddit("all").search(f"Ted Cruz, Using His Goldfish Brain, Attacks the NAACP for Florida Travel Advisory", limit=1)),
        next(api.reddit.subreddit("politics").search(f"Rick Scott issues travel advisory for ‘socialists,’ warning Florida is ‘openly hostile’ to them", limit=1)),
        next(api.reddit.subreddit("inthenews").search(f"Ted Cruz said Martin Luther King Jr. would be 'ashamed' of the NAACP's Florida travel warning. MLK's daughter, Bernice King, disagreed.", limit=1)),
        next(api.reddit.subreddit("AdviceAnimals").search(f"The NAACP is right", limit=1)),
        next(api.reddit.subreddit("PropagandaPosters").search(f"NAACP Anti Lynching Poster early 1930s", limit=1)),
        next(api.reddit.subreddit("todayilearned").search(f"TIL Frank Sinatra was an avid supporter of civil rights. He was a generous financial supporter of Martin Luther King Jr, and was recruited by him to join the civil rights marches in the south. He would go on to receive a lifetime award from the NAACP.", limit=1)),
    ]
    title = 'NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under Gov. DeSantis’ administration'
    url = "https://www.cnn.com/2023/05/21/us/naacp-florida-travel-advisory/index.html"
    raise NotImplementedError
    api.check_submissions_relevance(submissions, title, url)


@pytest.mark.reddit
def test_get_comments():
    submission = next(api.reddit.subreddit("politics").search(f"url: https://www.cnn.com/2023/05/21/us/naacp-florida-travel-advisory/index.html", limit=1))
    comments = api.get_submission_comments(submission)
    assert type(comments) == list
    assert type(comments[0]) == str
    assert len(comments) > 400


def test_use_comments_to_check_claims():
    # TODO: parse comments to get objections to claims from article
    claims = [
        Claim(
            id=0,
            claim='The NAACP has issued a travel advisory for Florida due to '
            "Governor Ron DeSantis' policies."
        ),
        Claim(
            id=1,
            claim="The travel advisory is in response to DeSantis' attempts to "
            'erase Black history and restrict diversity, equity, and '
            'inclusion programs in Florida schools.'
        ),
        Claim(
            id=2,
            claim='The advisory warns that Florida is openly hostile towards '
            'African Americans, people of color, and LGBTQ+ individuals.'
        ),
        Claim(
            id=3,
            claim='The League of United Latin American Citizens (LULAC) has also '
            "issued a travel advisory for Florida due to DeSantis' policies."
        ),
        Claim(
            id=4,
            claim='DeSantis has banned the teaching of critical race theory in '
            'Florida schools.'
        ),
        Claim(
            id=5,
            claim='DeSantis has supported legislation barring instruction that '
            'suggests anyone is privileged or oppressed based on their race '
            'or skin color.'
        ),
        Claim(
            id=6,
            claim="DeSantis' administration blocked a preliminary version of a new "
            'Advanced Placement course for high school students on African '
            'American studies.'
        ),
        Claim(
            id=7,
            claim="Florida's new concealed weapon law allows gun owners to carry a "
            'concealed weapon without a permit or training.'
        ),
        Claim(
            id=8,
            claim='The NAACP distributed 10,000 books to predominantly Black '
            "communities across Florida after DeSantis' administration "
            'rejected the AP African American studies course.'
        ),
        Claim(
            id=9,
            claim='The NAACP encourages local branches and youth councils to start '
            'community libraries to ensure access to representative '
            'literature.'
        ),
        Claim(
            id=10,
            claim='The NAACP has previously issued a travel advisory for Missouri '
            'due to a law that made it more difficult for employees to prove '
            'their protected class.'
        ),
    ]
    comments = [
        # TODO: select some comments
    ]
    # TODO: examine claim_checks
    claim_checks = api.use_comments_to_check_claims(comments, claims)
