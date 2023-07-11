// function to check if URL is a news article
export function is_news_article_url(url) {
    const news_urls = [  // RegExp objects
        /^https:\/\/www\.foxnews\.com\/(?!opinion\/)[^\/]+\/[^\/]+\/?.*$/,
        /^https:\/\/www\.cnn\.com\/\d{4}\/\d{2}\/\d{2}\/(?!opinions).*\/[^\/]+\/index\.html$/
    ]
    // TODO: return name of news site (change function name to get_article_type_from_url, include news, opinion, etc. along with source)
    return news_urls.some((re) => re.test(url.href));
}
