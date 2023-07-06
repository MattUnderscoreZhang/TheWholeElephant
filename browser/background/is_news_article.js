// function to check if URL is a news article
export function is_news_article_url(url) {
    const news_urls = [  // RegExp objects
        /^https:\/\/www\.foxnews\.com\/(?!opinion\/)[^\/]+\/[^\/]+\/?.*$/,
        /^https:\/\/www\.cnn\.com\/\d{4}\/\d{2}\/\d{2}\/(?!opinions).*\/[^\/]+\/index\.html$/
    ]
    return news_urls.some((re) => re.test(url.href));
}
