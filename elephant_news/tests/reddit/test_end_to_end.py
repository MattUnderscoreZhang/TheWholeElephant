from collections import defaultdict
import pytest

from elephant_news.analysis import claims
from elephant_news.reddit import api


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
