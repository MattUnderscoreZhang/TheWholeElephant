from dataclasses import dataclass

from elephant_news.analysis.claims import Claim
from elephant_news.analysis.snippets import Snippet
from elephant_news.analysis.sources import Source
from elephant_news.analysis.viewpoints import ClaimAnalysis


@dataclass
class Article:
    title: str
    text: str
    related_articles: list[str]


# from https://www.foxnews.com/media/simply-ignore-says-florida-black-business-owner-about-naacps-travel-advisory
article = Article(
    title = "‘Simply ignore it' says Florida Black business owner about NAACP's travel advisory",
    text = """
A Florida Black business owner said travelers thinking about vacationing in the Sunshine State should ignore the NAACP’s recent travel advisory.

"I would tell Black people who have seen this advisory to not come to Florida to simply ignore it," Mike Hill, the owner of an independent insurance and financial services agency in Pensacola, told Fox News Digital.

The NAACP’s travel advisory, issued earlier this week, accused Florida of being "hostile toward African Americans, people of color and LGBTQ+ individuals." The organization said in a press release that the action was "in direct response to Governor Ron DeSantis' aggressive attempts to erase Black history and to restrict diversity, equity, and inclusion programs in Florida schools." It also cited various bills the governor recently signed including restrictions on abortion, the new constitutional carry law, and the ban on funding for DEI programs at Florida’s public universities.

"Before traveling to Florida, please understand that the state of Florida devalues and marginalizes the contributions of, and the challenges faced by African Americans and other communities of color," the statement read.

But Hill accused the NAACP of putting out the statement, which received extensive media attention, to help fundraise.

"I believe that they see the amount of tens of millions of dollars that Black Lives Matter has been able to raise from the leftist agenda, and so they want a part of that gravy train," he said. "I believe it was more a publicity stunt. It was an attempt to fundraise more than anything else."

Hill also claimed the statement was put out now as "fodder" to use against DeSantis while he is running for president, as the Florida governor officially entered the 2024 field this week. And Hill pointed out that the NAACP’s Board of Directors chairman, Leon W. Russell, lives in the Tampa area.

"The irony that he has lived here most of his adult life, has actually witnessed the fact that a thousand people a day move to Florida for the opportunity that's here and that he would still issue out a statement saying don't come here because of the racist attitudes that exist in Florida," Hill said. 

DeSantis blasted the NAACP's travel advisory as a "political stunt" during his conversation with Elon Musk on Twitter's "Spaces" platform Wednesday evening when he announced his presidential campaign.

"Claiming that Florida is unsafe is a total farce," he said.

Hill, who is also part of an initiative promoting Black Americans called Project 21, said the NAACP's actions would only hurt the organization going forward. 

"I don't think is going to deter anyone from coming to Florida," he said. "If anything, I think this is going to backfire on the NAACP and show just how irrelevant they've become as an organization." 

To hear more from the Florida business owner, click here.
    """,
    related_articles = [
        "GIANNO CALDWELL SLAMS NAACP OVER FLORIDA TRAVEL ADVISORY: ‘PUT ONE OUT IN CHICAGO’",
        "NAACP LEADER DEFENDS LIVING IN FLORIDA DESPITE ORG'S TRAVEL WARNING: ‘WE HAVEN’T TOLD ANYBODY TO LEAVE'",
        "TWITTER SPACES MELTDOWN DURING DESANTIS ANNOUNCEMENT SPARKS SCORCHED EARTH REACTION FROM TRUMP SUPPORTERS",
    ],
)


article_text = article.title + "\n" + article.text + "\n" + "Related articles:\n" + "\n".join(article.related_articles)


claims = [
    Claim(
        id=0,
        claim='Mike Hill, a Black business owner in Florida, advises Black '
        "people to ignore the NAACP's recent travel advisory about the "
        'state.',
        source='Mike Hill, owner of an independent insurance and financial '
        'services agency in Pensacola, Florida, in an interview with Fox '
        'News Digital.'
    ),
    Claim(
        id=1,
        claim='The NAACP issued a travel advisory accusing Florida of being '
        'hostile towards African Americans, people of color, and LGBTQ+ '
        'individuals.',
        source='The NAACP in a press release.'
    ),
    Claim(
        id=2,
        claim='The NAACP issued the travel advisory in response to Governor Ron '
        "DeSantis' attempts to erase Black history and restrict "
        'diversity, equity, and inclusion programs in Florida schools.',
        source='The NAACP in a press release.'
    ),
    Claim(
        id=3,
        claim='The NAACP cited various bills recently signed by Governor '
        'DeSantis, including restrictions on abortion, the new '
        'constitutional carry law, and the ban on funding for DEI '
        "programs at Florida's public universities.",
        source='The NAACP in a press release.'
    ),
    Claim(
        id=4,
        claim='Mike Hill accused the NAACP of putting out the statement to '
        'fundraise and to use against DeSantis while he is running for '
        'president.',
        source='Mike Hill, owner of an independent insurance and financial '
        'services agency in Pensacola, Florida, in an interview with Fox '
        'News Digital.'
    ),
    Claim(
        id=5,
        claim="Mike Hill claimed that the NAACP's Board of Directors chairman, "
        'Leon W. Russell, lives in the Tampa area.',
        source='Mike Hill, owner of an independent insurance and financial '
        'services agency in Pensacola, Florida, in an interview with Fox '
        'News Digital.'
    ),
    Claim(
        id=6,
        claim="Mike Hill said that the NAACP's actions would only hurt the "
        'organization going forward.',
        source='Mike Hill, owner of an independent insurance and financial '
        'services agency in Pensacola, Florida, in an interview with Fox '
        'News Digital.'
    ),
    Claim(
        id=7,
        claim="Governor DeSantis called the NAACP's travel advisory a political "
        'stunt.',
        source='Governor Ron DeSantis on Twitter\'s "Spaces" platform.'
    ),
]


sources = [
    Source(
        id=0,
        description='NAACP issues travel advisory for Florida, citing '
        'hostility towards African Americans, people of color, and '
        'LGBTQ+ individuals',
        source_type='press_release',
        is_primary_source=True,
        is_available_online=True
    ),
    Source(
        id=1,
        description='Interview with Mike Hill, owner of an independent '
        'insurance and financial services agency in Pensacola, '
        "Florida, who advises Black people to ignore the NAACP's "
        'travel advisory',
        source_type='interview',
        is_primary_source=True,
        is_available_online=True
    ),
    Source(
        id=2,
        description="Florida Governor Ron DeSantis calls the NAACP's travel "
        "advisory a 'political stunt'",
        source_type='speech',
        is_primary_source=False,
        is_available_online=True
    ),
    Source(
        id=3,
        description="Article reporting on Gianno Caldwell's criticism of the "
        "NAACP's travel advisory and Leon W. Russell's defense of "
        'living in Florida despite the advisory',
        source_type='article',
        is_primary_source=False,
        is_available_online=True
    ),
    Source(
        id=4,
        description='Article reporting on Twitter Spaces meltdown during '
        'DeSantis announcement and reaction from Trump supporters',
        source_type='article',
        is_primary_source=False,
        is_available_online=True
    ),
]


snippets = [
    Snippet(
        id=0,
        snippet='A Florida Black business owner said travelers thinking about '
        'vacationing in the Sunshine State should ignore the NAACP’s '
        'recent travel advisory.',
        claim_ids=[0],
        source_ids=[1],
    ),
    Snippet(
        id=1,
        snippet='The NAACP’s travel advisory, issued earlier this week, '
        'accused Florida of being "hostile toward African Americans, '
        'people of color and LGBTQ+ individuals."',
        claim_ids=[1],
        source_ids=[0],
    ),
    Snippet(
        id=2,
        snippet='The organization said in a press release that the action was '
        '"in direct response to Governor Ron DeSantis\' aggressive '
        'attempts to erase Black history and to restrict diversity, '
        'equity, and inclusion programs in Florida schools."',
        claim_ids=[2],
        source_ids=[0],
    ),
    Snippet(
        id=3,
        snippet='It also cited various bills the governor recently signed '
        'including restrictions on abortion, the new constitutional '
        'carry law, and the ban on funding for DEI programs at '
        'Florida’s public universities.',
        claim_ids=[3],
        source_ids=[0],
    ),
    Snippet(
        id=4,
        snippet='Mike Hill accused the NAACP of putting out the statement, '
        'which received extensive media attention, to help fundraise.',
        claim_ids=[4],
        source_ids=[],
    ),
    Snippet(
        id=5,
        snippet='Mike Hill also claimed the statement was put out now as '
        '"fodder" to use against DeSantis while he is running for '
        'president, as the Florida governor officially entered the '
        '2024 field this week.',
        claim_ids=[5],
        source_ids=[],
    ),
    Snippet(
        id=6,
        snippet='Mike Hill pointed out that the NAACP’s Board of Directors '
        'chairman, Leon W. Russell, lives in the Tampa area.',
        claim_ids=[6],
        source_ids=[],
    ),
    Snippet(
        id=7,
        snippet="DeSantis blasted the NAACP's travel advisory as a "
        '"political stunt" during his conversation with Elon Musk on '
        'Twitter\'s "Spaces" platform Wednesday evening when he '
        'announced his presidential campaign.',
        claim_ids=[7],
        source_ids=[2],
    ),
    Snippet(
        id=8,
        snippet="Mike Hill believes the NAACP's actions will hurt the "
        'organization going forward.',
        claim_ids=[8],
        source_ids=[],
    ),
]


viewpoints = [
    ClaimAnalysis(id=0, support_ids=[], refute_ids=[], is_opinion=True),
    ClaimAnalysis(id=1, support_ids=[2, 3], refute_ids=[], is_opinion=False),
    ClaimAnalysis(id=2, support_ids=[], refute_ids=[], is_opinion=True),
    ClaimAnalysis(id=3, support_ids=[], refute_ids=[], is_opinion=False),
    ClaimAnalysis(id=4, support_ids=[], refute_ids=[1], is_opinion=True),
    ClaimAnalysis(id=5, support_ids=[], refute_ids=[1], is_opinion=True),
    ClaimAnalysis(id=6, support_ids=[], refute_ids=[1], is_opinion=True),
    ClaimAnalysis(id=7, support_ids=[1], refute_ids=[], is_opinion=True),
    ClaimAnalysis(id=8, support_ids=[], refute_ids=[1], is_opinion=True),
]
