from collections import defaultdict
import pytest

from elephant_news.analysis import claims
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


# @pytest.mark.reddit
def test_end_to_end_claim_check():
    url = "https://www.foxnews.com/politics/grassley-burisma-executive-who-allegedly-paid-biden-has-audio-recordings-of-conversations-with-joe-hunter"
    title = "Grassley: Burisma executive who allegedly paid Biden has audio recordings of conversations with Joe, Hunter"
    article_text = '''
Sen. Chuck Grassley said Monday that the Burisma executive who allegedly paid Joe Biden and Hunter Biden kept 17 audio recordings of his conversations with them as an "insurance policy," citing the FBI FD-1023 form that the bureau briefed congressional lawmakers on. 

Grassley, R-Iowa, revealed from the Senate floor Monday what was said to be a redacted reference in the FBI-generated FD-1023 form alleging a criminal bribery scheme between then-Vice President Joe Biden and a foreign national that involved influence over U.S. policy decisions.

Fox News Digital exclusively reported on the contents of the form last week. The FD-1023 form, dated June 30, 2020, is the FBI's interview with a "highly credible" confidential source who detailed multiple meetings and conversations he or she had with a top Burisma executive over the course of several years, starting in 2015. Fox News Digital has not seen the form, which is redacted, but it was described by several sources who are aware of its contents.

Grassley said the FD-1023 has a redacted reference that the Burisma executive possesses fifteen audio recordings of phone calls between himself and Hunter Biden.

According to Grassley, the FD-1023 also states that the executive possesses two audio recordings of phone calls between himself and then-Vice President Joe Biden.

Grassley, from the Senate floor, slammed the FBI for not complying with the House Oversight Committee’s subpoena, saying Congress "still lacks a full and complete picture with respect to what that document really says."

"That’s why it’s important that the document be made public without unnecessary redactions for the American people to see," he said. "Let me assist for purposes of transparency."

"The 1023 produced to that House Committee redacted reference that the foreign national who allegedly bribed Joe and Hunter Biden allegedly has audio recordings of his conversations with them," Grassley continued. "17 total recordings."

"According to the 1023, the foreign national possesses 15 audio recordings of phone calls between him and Hunter Biden," Grassley said. "According to the 1023, the foreign national possesses two audio recordings of phone calls between him and then-Vice President Joe Biden."

Grassley said the recordings were "allegedly kept as a sort of insurance policy for the foreign national in case he got into a tight spot."

"The 1023 also indicates that then-Vice President Joe Biden may have been involved in Burisma employing Hunter Biden," Grassley said.

Grassley demanded answers on "what, if anything has the Justice Department and FBI done to investigate?"

"The Justice Department and FBI must show their work," Grassley said. "They no longer deserve the benefit of the doubt."

The FBI brought the document to Capitol Hill last week after House Oversight Committee Chairman James Comer subpoenaed it last month. The FBI briefed Comer and committee Ranking Member Jamie Raskin, D-Md., on the form in a SCIF on Capitol Hill, but did not turn over the document. Comer threatened to hold FBI Director Christopher Wray in contempt of Congress.

The FBI made a further accommodation and later brought the form to a secure setting on Capitol Hill for all Oversight Committee members to view, but the document is still not in the committee's possession. 

A source familiar told Fox News Digital on Monday that the FBI did not redact the section of the FD-1023 referencing the audio recordings when showing the document to solely to Comer and Raskin, but did so for the full committee briefing. The source said Grassley and Comer had already seen the form, even prior to the FBI sharing it with Congress.

Fox News Digital was exclusively briefed on the contents of the form last week. 

Sources told Fox News Digital that the confidential human source told the FBI that the Burisma executive was speaking with the confidential source to "get advice on the best way to go forward" in 2015 and 2016 in gaining U.S. oil rights and getting involved with a U.S. oil company. 

According to the FD-1023 form, the confidential human source said the Burisma executive discussed Hunter’s role on the board. The confidential human source questioned why the Burisma executive needed his or her advice in acquiring access to U.S. oil if he had Hunter Biden on the board. The Burisma executive answered by referring to Hunter Biden as "dumb."

The Burisma executive explained to the confidential source that Burisma had to "pay the Bidens" because Ukrainian prosecutor Viktor Shokin was investigating Burisma, and explained how difficult it would be to enter the U.S. market in the midst of that investigation.

The confidential source further detailed that conversation, suggesting to the Burisma executive that he "pay the Bidens $50,000 each," to which the Burisma executive replied, it is "not $50,000," it is "$5 million."

"$5 million for one Biden, $5 million for the other Biden," the Burisma executive told the confidential human source, according to a source familiar with the document.

A source familiar said according to the document, the $5 million payments appeared to reference a kind of "retainer" Burisma intended to pay the Bidens to deal with a number of issues, including the investigation led by Shokin. Another source referred to the arrangement as a "pay-to-play" scheme. 

Sources familiar told Fox News Digital that the confidential human source believes that the $5 million payment to Joe Biden and the $5 million payment to Hunter Biden occurred, based on his or her conversations with the Burisma executive. 

The confidential source said the Burisma executive told him he "paid" the Bidens in such a manner "through so many different bank accounts" that investigators would not be able to "unravel this for at least 10 years."

The document then makes reference to "the Big Guy," which, has been said to be a reference to Joe Biden.

The Burisma executive told the confidential source that he "didn’t pay the Big Guy directly." 

Sources said the Burisma executive appears to be at a "very, very high level" of the company. One source familiar suggested the confidential source could be referring to the head of Burisma, Mykola Zlochevsky, but said the name of the Burisma executive is redacted in the document.

Biden has acknowledged that when he was vice president, he successfully pressured Ukraine to fire prosecutor Viktor Shokin. At the time, Shokin was investigating Burisma Holdings, and at the time, Hunter had a highly-lucrative role on the board receiving thousands of dollars per month. The then-vice president threatened to withhold $1 billion of critical U.S. aid if Shokin was not fired.

The confidential source, according to the sources familiar with the FD-1023 form, told the Burisma executive he should "get away" from the Bidens and said the executive should "not want to be involved" with them.

A source familiar with the document told Fox News Digital that the confidential human source goes on to detail a later conversation with the Burisma executive following the 2016 presidential election. The confidential source asked the Burisma executive if he was "upset" that Donald Trump won.

The source said the Burisma executive told the confidential source that he was "an oracle," referring to his or her advice to "get away" from the Bidens due to fears of potential investigations into their dealings. 

The White House has maintained that President Biden has never been involved in his son's business dealings and has never discussed them with him. And it has noted that removing Shokin was administration policy at the time.

Hunter Biden is currently under federal investigations for his "tax affairs." The investigation began in 2018 and was prompted by suspicious foreign transactions. 

The White House declined to comment, pointing to a statement by Joe Biden Thursday calling the allegations "a bunch of malarky."
    '''
    article_claims = claims.list_claims(article_text)
    submissions = api.get_submissions_matching_url(url, 2)
    # api.check_submissions_relevance(submissions, title, url)
    all_claim_checks = []
    for submission in submissions:
        comments = api.get_submission_comments(submission)
        claim_checks = api.use_comments_to_check_claims(comments, article_claims)
        all_claim_checks.extend(claim_checks)
    dict_claim_checks = defaultdict(list)
    for claim_checks in all_claim_checks:
        dict_claim_checks[claim_checks.claim_id].append(claim_checks.objections)
    breakpoint()
