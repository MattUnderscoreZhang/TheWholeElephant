import {is_news_article_url} from "../background/is_news_article.js";


describe("is_news_article_url", function() {
    describe("Fox News", function() {
        it("Not Articles", function() {
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/politics")), false);
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/world")), false);
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/opinion")), false);
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/some_category")), false);
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/some_category/")), false);
        })

        it("News Articles", function() {
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/politics/news_article")), true);
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/world/news_article")), true);
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/some_category/news_article")), true);
        })

        it("Opinion Articles", function() {
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com/opinion/opinion_article")), false);
        })
    })

    describe("Other", function() {
        it("Unrecognized URL", function() {
            assert.equal(is_news_article_url(new URL("https://www.google.com/")), false);
            assert.equal(is_news_article_url(new URL("https://www.google.com/blah")), false);
            assert.equal(is_news_article_url(new URL("https://www.google.com/blah/not_news_article")), false);
        })
    })
})
