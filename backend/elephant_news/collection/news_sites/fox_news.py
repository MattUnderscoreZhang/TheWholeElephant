from dataclasses import dataclass
from bs4 import BeautifulSoup as BS
from typing import cast


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


def parse(html: str) -> Article:
    soup = BS(html)

    article_header = cast(BS, soup.find('header', class_='article-header'))
    headline = cast(BS, article_header.find('h1', class_='headline')).text
    sub_headline = cast(BS, article_header.find('h2', class_='sub-headline')).text
    author_div = cast(BS, article_header.find('div', class_='author-byline'))
    author = cast(BS, author_div.find('a')).text

    article_body = cast(BS, soup.find('div', class_='article-body'))
    paragraphs = cast(BS, article_body.find_all('p', recursive=False))
    non_link_paragraphs = [p for p in paragraphs if not cast(BS, p).find('strong')]
    article_text = "\n".join([p.text for p in non_link_paragraphs])
    article_text = article_text.replace("\xa0", "")
    article_text = article_text.replace("\n", "")

    article_links = [cast(BS, p).find('a') for p in non_link_paragraphs if cast(BS, p).find('a')]
    article_links = [cast(BS, link) for link in article_links]
    article_links = {link.text: cast(URL, link['href']) for link in article_links}

    non_article_paragraphs = [p for p in paragraphs if cast(BS, p).find('strong')]
    non_article_links = [cast(BS, p).find('a') for p in non_article_paragraphs if cast(BS, p).find('a')]
    non_article_links = [cast(BS, link) for link in non_article_links]
    non_article_links = {link.text: cast(URL, link['href']) for link in non_article_links}
    non_article_links.pop("CLICK HERE TO GET THE FOX NEWS APP")

    article_images = cast(BS, article_body.find_all('picture'))
    article_images = [cast(BS, image).find('img') for image in article_images]
    article_images = [cast(BS, image) for image in article_images]
    article_images = {cast(str, image['alt']): cast(URL, image['src']) for image in article_images}

    video_containers = cast(BS, article_body.find_all('div', class_='video-container'))
    video_infos = [cast(BS, container.find_next_sibling('div', class_='info')) for container in video_containers]
    video_captions = [cast(BS, info.find('div', class_='caption')) for info in video_infos]
    article_videos = {caption.text: cast(URL, cast(BS, caption.find('a'))['href']) for caption in video_captions}

    # TODO: extract comments

    article = Article(
        headline=headline,
        sub_headline=sub_headline,
        author=author,
        text=article_text,
        links=article_links,
        images=article_images,
        videos=article_videos,
    )

    return article
