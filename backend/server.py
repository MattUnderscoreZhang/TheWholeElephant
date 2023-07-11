from fastapi import FastAPI
from pydantic import BaseModel

from elephant_news.reddit import api


app = FastAPI()


class PageInfo(BaseModel):
    url: str
    body: str


@app.post("/analyze_page")
def sendpage(page_info: PageInfo) -> str:
    from elephant_news.collection.news_sites.fallback import parse
    article = parse(page_info.body)
    response = api.reddit_article_check(page_info.url, str(article))
    return response
