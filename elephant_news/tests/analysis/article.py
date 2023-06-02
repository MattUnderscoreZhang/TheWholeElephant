from dataclasses import dataclass


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
