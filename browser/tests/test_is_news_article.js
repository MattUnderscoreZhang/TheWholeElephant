import {is_news_article_url} from "../background/is_news_article.js";


export let tests = describe("is_news_article_url", function() {
    describe("Fox News", function() {
        it("Not Articles", function() {
            assert.equal(is_news_article_url(new URL("https://www.foxnews.com")), false);
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

    describe("CNN", function() {
        it("Not Articles", function() {
            assert.equal(is_news_article_url(new URL("https://www.cnn.com")), false);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/world")), false);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/world/americas")), false);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/entertainment/tv-shows")), false);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/some_category/")), false);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/2023/07/05/category/index.html")), false);
        })

        it("News Articles", function() {
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/2023/07/05/entertainment/daniel-radcliffe-harry-potter-tv-series/index.html")), true);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/2023/07/05/us/philadelphia-shooting-wednesday/index.html")), true);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/2023/07/05/politics/taylor-taranto-detention-memo-obama-neighborhood-arrest/index.html")), true);
        })

        it("Opinion Articles", function() {
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/2023/07/04/opinions/supreme-court-online-harassment-university-of-chicago-alaimo/index.html")), false);
            assert.equal(is_news_article_url(new URL("https://www.cnn.com/2023/06/30/opinions/student-loan-ruling-shows-trumps-supreme-court-plan-litman/index.html")), false);
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
