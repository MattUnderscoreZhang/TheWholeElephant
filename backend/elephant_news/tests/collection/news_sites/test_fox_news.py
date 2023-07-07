from pathlib import Path

from elephant_news.collection.news_sites.fox_news import parse


def test_parse():
    html_file = Path(__file__).parent.parent.parent / "data" / "html" / "2023_07_05_fox_prigozhin.html"
    with open(html_file, "r") as f:
        article = parse(f.read())
    assert article.headline == "Mercenary warlord Prigozhin breaks silence following Belarus exile in message to Russian people: report"
    assert article.sub_headline == "Yevgeny Prigozhin has allegedly returned to Russia since his exile started"
    assert article.author == "Peter Aitken"
    assert "Russian mercenary warlord-turned-rebel Yevgeny Prigozhin appeared to call on the Russian public to join the Wagner Group" in article.text
    assert article.links == {
        'audio posted': 'https://t.me/grey_zone/19396',
        '‘March of Justice’': 'https://www.foxnews.com/politics/us-spy-agencies-intel-mid-june-wagner-chief-prigozhin-planning-armed-action-russia-report',
        'abruptly ended the operation': 'https://www.foxnews.com/world/wagner-chief-orders-troops-turn-around-from-moscow-avoid-bloodshed',
        'military purge reportedly followed': 'https://www.foxnews.com/world/pentagon-addresses-rumors-russian-military-purge-following-short-lived-wagner-mutiny',
        'returned to Russia': 'https://www.fontanka.ru/2023/07/05/72464159/',
        'shuttered his media holdings': 'https://www.foxnews.com/world/wagner-boss-prigozhin-shutters-patriot-media-operations',
        'Wagner building a new military base': 'https://www.foxnews.com/world/european-satellite-imagery-appears-show-wagner-building-up-military-base-belarus-russia-mutiny',
        'Defense Department': 'https://www.foxnews.com/category/politics/defense'
    }
    assert article.images == {
        'Mercenary leader Prigozhin threatens Kremlin leadership ': 'https://a57.foxnews.com/cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/9da0e509-1e7a-4e43-9281-5a60cf310260/a7d92da1-8cb2-4bb1-8e71-ffdd8aea0997/1280x720/match/896/500/image.jpg?ve=1&tl=1',
        'Wagner Group chief Yevgeny Prigozhin leaves Rustov in an SUV after his armed rebellion against the Russian military was called off': 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/06/640/320/yevgeny-prigozhin-leaves-rustov-suv-wagner-group-mutiny.jpg?ve=1&tl=1',
        'Russian President Vladimir Putin sits next to Russian General Staff Valery Gerasimov': 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/06/640/320/vladimir-putin-valery-gerasimov-russian-general-wagner-group-mutiny.jpg?ve=1&tl=1',
        'Wagner Group military company seen in Russia': 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/06/640/320/AP23175782763608.jpg?ve=1&tl=1'
    }
    assert article.videos == {
        "Mercenary leader Prigozhin threatens Kremlin leadership  Fox News senior foreign affairs correspondent Greg Palkot has the latest on Wagner leader Yevgeny Prigozhin accusing Russian forces of attacking his troops on 'Special Report.'": 'https://www.foxnews.com/video/6330321765112'
    }
