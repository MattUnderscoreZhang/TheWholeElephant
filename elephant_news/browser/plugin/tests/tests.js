describe("is_news_article_url", function() {
    it("Fox News - Not Articles", function() {
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/politics")), false);
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/world")), false);
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/opinion")), false);
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/some_category")), false);
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/some_category/")), false);
    })

    it("Fox News - News Articles", function() {
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/politics/news_article")), true);
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/world/news_article")), true);
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/some_category/news_article")), true);
    })

    it("Fox News - Opinion Articles", function() {
        assert.equal(is_news_article_url(new URL("https://www.foxnews.com/opinion/opinion_article")), false);
    })

    it("Unrecognized URL", function() {
        assert.equal(is_news_article_url(new URL("https://www.google.com/")), false);
    })
})
