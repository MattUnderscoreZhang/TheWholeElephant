from bs4 import BeautifulSoup as BS
from dataclasses import dataclass
import json

from elephant_news.llm.llm import ask


URL = str


@dataclass
class Article:
    headline: str
    sub_headline: str
    author: str
    text: str
    links: dict[str, URL]
    images: dict[str, URL]
    videos: dict[str, URL]


def extract_text(html: str) -> str:
    soup = BS(html, 'html.parser')
    article_text = soup.get_text()
    clean_text = ask(f"""
        Please take the text in triple quotes below, extracted from a website, and return a cleanly formatted article with the irrelevant text removed.
        Make sure to remove newlines and other formatting symbols.

        '''
        {article_text}
        '''
    """)
    # TODO: add test
    return clean_text


def extract_article(text: str) -> Article:
    reply = ask(f"""
        Please take the news article text in triple quotes below, and extract information in the following JSON format, where URL is a str type.

        {{
          headline: str,
          sub_headline: str,
          author: str,
          text: str,
          links: {{
            str: URL
          }},
          images: {{
            str: URL
          }},
          videos: {{
            str: URL
          }}
        }}

        '''
        {text}
        '''
    """)
    article = Article(**json.loads(reply))
    # TODO: add test
    return article


def parse(html: str) -> Article:
    article_text = extract_text(html)
    article = extract_article(article_text)
    return article
