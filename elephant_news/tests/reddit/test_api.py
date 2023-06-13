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


@pytest.mark.reddit
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
        "Florida just lost $1B in Disney investment too. They are losing tourism dollars too. DeFascists is so dumb.",
        "I'm not a fan of DeSantis, but this is a bit of a stretch. The NAACP is just saying this for political reasons.",
        '''
        Florida man here. I was hanging with my Grandma and she said the quiet parts out loud but whats so frightening is the “I just saw it, I know it” attitude towards this shit.

Ill list examples below, her side of my family shares beliefs and her info is spoon-fed by her daughter/church/whatever news she uses now that Faux is “woke”.

LGBTQ & Drag Queens: She believes that they are being recruited to teach children to become trans and groom them. Also George Soros is involved, public schools are “all groomers”.

Immigration: Apparently we hand them cash, a phone and free housing to illegal immigrants. That Homeless Veteran video REALLY worked on these morons.

Woke: To them, “Woke is anything not conservative, its pure evil”. The list of what to hate is so large that they use this.

Public Schools: They HATE public schools. “Parents should get All the taxes they spent on public schools refunded so they can pay for private schools”.

Florida is gone, I’m waiting for their party to openly declare public schools are “Woke” but not sure if thats before or after they’d round up the “Woke”- which “needs to happen and soon”.
        ''',
        '''
        So, Tiny D has made Florida a place where education, tourism, employment and healthcare are dead not a priority.

Homeownership was already not happening for any non-boomers.

Florida really is about to be the Sunset State where you go to die alone with your bigoted kin.

Edit: reworded the first part, will remove edit when ‘23 data is released from a non-FL source.
        ''',
        "Because he didn’t add AP African American History to the offered high school classes? That’s the reason people can’t vacation in FL?",
        '''
        Florida used to be "openly hostile" to people of color.

They still are. But they used to be too.
        ''',
        "It's because they get equal treatment, not preferential treatment",
        "Why aren’t the Jewish people upset too? Isn’t teaching the holocaust banned down there?",
        '''
Do you honestly believe that's the case? Is that really what left wing news is reporting? Its been Florida law since 94 to teach the Holocaust in all k-12 schools in Florida. Every year there is holocaust memorial week in Florida schools and just a couple years ago DeSantis passed legislation to standardize teachings that were praised by the Jewish Media. DeSantis was literally just in Israel and passed legislation to combat anti-Semitism.

https://www.flgov.com/2023/04/28/governor-ron-desantis-signs-enhanced-anti-antisemitism-and-anti-bds-legislation-in-israel/

https://www.jns.org/florida-makes-strides-in-holocaust-education-after-new-standards-prioritize-source-material/
        ''',
        "Patiently waiting for an article to come out about NAACP members taking summer vacations to Florida.",
        '''
        Lol. I live in Florida. There are all types of complexion at the bars. Everyone gets along fine.

The NAAPOC displays petty racism once again...
        ''',
        "Why doesn’t the NAACP advise them to avoid Chicago, St Louis, Memphis, Jackson, Baltimore, Detroit, Philadelphia, Oakland, Shreveport, or Milwaukee?",
        "Are you saying that the NAACP doesn’t care about their intended audience and only about partisan politics? Shocking.",
        "So if you do not hold the same political line as the liberal cultural elites, is the economic blockade and sabotage justified? Are they going to do the same with Florida as they did with Cuba? Indiscriminately attacking the entire state may not be the best way to subvert polarization, slapping someone in the face to get them to change their political views doesn't usually work. In addition, the levels of victimhood are exorbitant considering that democrats and progressives are in total control of the narrative.",
    ]
    claim_checks = api.use_comments_to_check_claims(comments, claims)
    assert len(claim_checks) == len(claims)
