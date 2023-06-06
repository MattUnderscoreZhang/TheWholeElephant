from dataclasses import dataclass

from elephant_news.analysis.claims import Claim
from elephant_news.analysis.snippets import Snippet
from elephant_news.analysis.sources import Source


@dataclass
class Article:
    title: str
    text: str
    related_articles: list[str]


# from https://www.cnn.com/2023/05/21/us/naacp-florida-travel-advisory/index.html
article = Article(
    title = "‘Beware, your life is not valued’: NAACP travel advisory warns Florida is ‘openly hostile toward African Americans’",
    text = """
Another advocacy group is warning people of color about traveling to Florida.

The alerts from groups representing Black and Latino Americans come as the state’s Republican governor, Ron DeSantis, is expected to enter the 2024 presidential race with a campaign built on tenets of the conservative agenda he’s fostered in Florida.

The NAACP issued a travel advisory for Florida “in direct response to … DeSantis’ aggressive attempts to erase Black history and to restrict diversity, equity, and inclusion programs in Florida schools,” the group said Saturday in a statement.

“Beware that your life is not valued,” NAACP President and CEO Derrick Johnson told CNN on Monday. He cited a new DeSantis-backed law allowing gun owners to carry a concealed weapon without a permit, as well as education policies that include a ban on teaching about gender identity and sexual orientation through 12th grade.

The announcement came days after LULAC – the League of United Latin American Citizens – issued a travel advisory for Florida after DeSantis signed a new immigration law that will go into effect in July.

Both LULAC and the NAACP say actions under the DeSantis administration are “hostile” to their communities.

“Florida is openly hostile toward African Americans, people of color and LGBTQ+ individuals,” the NAACP said. “Before traveling to Florida, please understand that the state of Florida devalues and marginalizes the contributions of, and the challenges faced by African Americans and other communities of color.”

Under DeSantis, Florida has banned the teaching of critical race theory, which acknowledges systemic racism is a part of American history and challenges the beliefs that allowed it to flourish. The governor said the concept would teach children “the country is rotten and that our institutions are illegitimate.”

DeSantis has supported legislation barring instruction that suggests anyone is privileged or oppressed based on their race or skin color. His administration also blocked a preliminary version of a new Advanced Placement course for high school students on African American studies, with Florida’s Department of Education saying it “significantly lacks educational value.”

The NAACP said DeSantis’ actions are “in direct conflict with the democratic ideals that our union was founded upon.”

“Let me be clear: Failing to teach an accurate representation of the horrors and inequalities that Black Americans have faced and continue to face is a disservice to students and a dereliction of duty to all,” said Johnson, the NAACP president.

CNN has sought comment from DeSantis’ office.

After the DeSantis administration rejected the AP African American studies course, the NAACP distributed 10,000 books to 25 predominantly Black communities across Florida in collaboration with the American Federation of Teachers’ Reading Opens the World program, the NAACP said.

The majority of the books donated were titles banned under the state’s increasingly restrictive laws. The NAACP continues to encourage local branches and youth councils to start community libraries to ensure access to representative literature.

The NAACP also decried Florida’s new concealed weapon law, which also states gun owners no longer have to take any training before carrying a concealed weapon outside the home. It goes into effect July 1.

The NAACP president said such measures are “not business-attractive policies” and urged members to consider holding conventions outside of Florida.

“The policies that he has put in place are harmful policies to far too many individuals,” Johnson said.

This isn’t the first time the NAACP has issued a travel advisory for a state. In 2017, the NAACP warned people of color about traveling to Missouri after the state passed Senate Bill 43, which made it more difficult for employees to prove their protected class, such as race or gender.

While the governor said the new law put Missouri’s standards for lawsuits in line with other states, the NAACP said it allows unlawful discrimination.
    """,
    related_articles = [
        "DeSantis proposes banning diversity and inclusion initiatives at Florida universities",
        "Race is left out of Rosa Parks' story in revised weekly lesson text",
        "DeSantis: Florida rejected AP course on African American studies due to 'political agenda'",
        "These 11 examples highlight aspects of critical race theory",
        "DeSantis signs bill allowing carry of concealed weapons without a permit",
    ],
)


article_text = article.title + "\n" + article.text + "\n" + "Related articles:\n" + "\n".join(article.related_articles)


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


sources = [
    Source(
        id=0,
        description="NAACP issues travel advisory for Florida due to DeSantis' "
        'policies',
        source_type='article',
        is_primary_source=True,
        is_available_online=True,
    ),
    Source(
        id=1,
        description='Interview with NAACP President and CEO Derrick Johnson',
        source_type='interview',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=2,
        description="LULAC issues travel advisory for Florida due to DeSantis' "
        'immigration law',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=3,
        description='DeSantis bans teaching of critical race theory in Florida',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=4,
        description='DeSantis administration blocks new Advanced Placement '
        'course on African American studies',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=5,
        description='NAACP distributes banned books to predominantly Black '
        'communities in Florida',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=6,
        description='DeSantis signs law allowing concealed carry without a '
        'permit',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=7,
        description='NAACP issues travel advisory for Missouri in 2017',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=8,
        description='DeSantis proposes banning diversity and inclusion '
        'initiatives at Florida universities',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=9,
        description="Rosa Parks' story revised to leave out race in weekly "
        'lesson text',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=10,
        description='DeSantis claims rejection of AP African American studies '
        "course due to 'political agenda'",
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
    Source(
        id=11,
        description='11 examples highlighting aspects of critical race theory',
        source_type='article',
        is_primary_source=False,
        is_available_online=True,
    ),
]


snippets = [
    Snippet(
        id=0,
        snippet='Another advocacy group is warning people of color about '
        'traveling to Florida.\n'
        '\n'
        'The alerts from groups representing Black and Latino '
        'Americans come as the state’s Republican governor, Ron '
        'DeSantis, is expected to enter the 2024 presidential race '
        'with a campaign built on tenets of the conservative agenda '
        'he’s fostered in Florida.\n'
        '\n'
        'The NAACP issued a travel advisory for Florida “in direct '
        'response to … DeSantis’ aggressive attempts to erase Black '
        'history and to restrict diversity, equity, and inclusion '
        'programs in Florida schools,” the group said Saturday in a '
        'statement.',
        claim_ids=[0, 1],
        source_ids=[0],
    ),
    Snippet(
        id=1,
        snippet='“Beware that your life is not valued,” NAACP President and '
        'CEO Derrick Johnson told CNN on Monday. He cited a new '
        'DeSantis-backed law allowing gun owners to carry a concealed '
        'weapon without a permit, as well as education policies that '
        'include a ban on teaching about gender identity and sexual '
        'orientation through 12th grade.',
        claim_ids=[1],
        source_ids=[1],
    ),
    Snippet(
        id=2,
        snippet='The announcement came days after LULAC – the League of '
        'United Latin American Citizens – issued a travel advisory '
        'for Florida after DeSantis signed a new immigration law that '
        'will go into effect in July.\n'
        '\n'
        'Both LULAC and the NAACP say actions under the DeSantis '
        'administration are “hostile” to their communities.',
        claim_ids=[3],
        source_ids=[2],
    ),
    Snippet(
        id=3,
        snippet='“Florida is openly hostile toward African Americans, people '
        'of color and LGBTQ+ individuals,” the NAACP said. “Before '
        'traveling to Florida, please understand that the state of '
        'Florida devalues and marginalizes the contributions of, and '
        'the challenges faced by African Americans and other '
        'communities of color.”',
        claim_ids=[2],
        source_ids=[0],
    ),
    Snippet(
        id=4,
        snippet='Under DeSantis, Florida has banned the teaching of critical '
        'race theory, which acknowledges systemic racism is a part of '
        'American history and challenges the beliefs that allowed it '
        'to flourish. The governor said the concept would teach '
        'children “the country is rotten and that our institutions '
        'are illegitimate.”',
        claim_ids=[4],
        source_ids=[3],
    ),
    Snippet(
        id=5,
        snippet='DeSantis has supported legislation barring instruction that '
        'suggests anyone is privileged or oppressed based on their '
        'race or skin color. His administration also blocked a '
        'preliminary version of a new Advanced Placement course for '
        'high school students on African American studies, with '
        'Florida’s Department of Education saying it “significantly '
        'lacks educational value.”',
        claim_ids=[5, 6],
        source_ids=[3, 4],
    ),
    Snippet(
        id=6,
        snippet='The NAACP said DeSantis’ actions are “in direct conflict '
        'with the democratic ideals that our union was founded '
        'upon.”\n'
        '\n'
        '“Let me be clear: Failing to teach an accurate '
        'representation of the horrors and inequalities that Black '
        'Americans have faced and continue to face is a disservice to '
        'students and a dereliction of duty to all,” said Johnson, '
        'the NAACP president.',
        claim_ids=[1, 4, 5],
        source_ids=[0, 3, 4],
    ),
    Snippet(
        id=7,
        snippet='The NAACP also decried Florida’s new concealed weapon law, '
        'which also states gun owners no longer have to take any '
        'training before carrying a concealed weapon outside the '
        'home. It goes into effect July 1.\n'
        '\n'
        'The NAACP president said such measures are “not '
        'business-attractive policies” and urged members to consider '
        'holding conventions outside of Florida.',
        claim_ids=[7],
        source_ids=[5],
    ),
    Snippet(
        id=8,
        snippet='After the DeSantis administration rejected the AP African '
        'American studies course, the NAACP distributed 10,000 books '
        'to 25 predominantly Black communities across Florida in '
        'collaboration with the American Federation of Teachers’ '
        'Reading Opens the World program, the NAACP said.\n'
        '\n'
        'The majority of the books donated were titles banned under '
        'the state’s increasingly restrictive laws. The NAACP '
        'continues to encourage local branches and youth councils to '
        'start community libraries to ensure access to representative '
        'literature.',
        claim_ids=[8, 9],
        source_ids=[5],
    ),
    Snippet(
        id=9,
        snippet='This isn’t the first time the NAACP has issued a travel '
        'advisory for a state. In 2017, the NAACP warned people of '
        'color about traveling to Missouri after the state passed '
        'Senate Bill 43, which made it more difficult for employees '
        'to prove their protected class, such as race or gender.\n'
        '\n'
        'While the governor said the new law put Missouri’s standards '
        'for lawsuits in line with other states, the NAACP said it '
        'allows unlawful discrimination.',
        claim_ids=[10],
        source_ids=[7],
    ),
]
