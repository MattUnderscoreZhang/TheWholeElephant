from elephant_news.reddit import api


def test_get_hot_threads_from_subreddit():
    threads = api.get_hot_threads_from_subreddit("wallstreetbets", 10)
    titles = [thread.title for thread in threads]
    assert len(titles) == 10
    assert all([type(title) == str for title in titles])


def test_get_threads_matching_url():
    url = "https://www.cnn.com/2023/05/21/us/naacp-florida-travel-advisory/index.html"
    threads = api.get_threads_matching_url(url, 10)
    titles = [thread.title for thread in threads]
    assert titles == [
        'NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under Gov. DeSantis’ administration',
        "NAACP issues travel advisory for Florida, saying the state is 'openly hostile toward African Americans' under Gov. DeSantis' administration | CNN",
        'NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under DeSantis due to the recent bans on Critical Race Theory in classrooms. According to Florida’s Department of Education, CRT “significantly lacks educational value.”',
        'NAACP issues travel advisory for Florida, saying the state is ‘openly hostile toward African Americans’ under Gov. DeSantis’ administration',
        'As someone who recently stays in Florida, I think they might have this backwards.... 🤣',
        "NAACP issues travel advisory for Florida, saying the state is 'openly hostile toward African Americans' under Gov. DeSantis' administration | CNN",
    ]
