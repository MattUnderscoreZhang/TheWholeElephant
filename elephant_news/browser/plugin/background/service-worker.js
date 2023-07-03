function is_news_article_url(url) {
    const news_urls = [  // RegExp objects
        /^https:\/\/www\.foxnews\.com\/(?!opinion\/)[^\/]+\/[^\/]+\/?.*$/
    ]

    return news_urls.some((re) => re.test(url.href));
}


// side panel opens when icon is clicked
chrome.sidePanel
    .setPanelBehavior({ openPanelOnActionClick: true })
    .catch((error) => console.error(error));


// side panel disables and auto-closes on non-news-article URLs
chrome.tabs.onUpdated.addListener(async (tabId, info, tab) => {
    if (!tab.url) return;
    const url = new URL(tab.url);
    if (is_news_article_url(url)) {
        await chrome.sidePanel.setOptions({
            tabId,
            path: "side_panel/analysis_panel.html",
            enabled: true
        });
        //await chrome.sidePanel.open(
            //OpenOptions = {},
            //(windowId) => { console.log("Opened"); }
        //);
    } else {
        await chrome.sidePanel.setOptions({
            tabId,
            path: "side_panel/manual_panel.html",
            enabled: true
        });
    }
});


chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "chat" || request.action === "sendpage") {
        console.log("Hello");
        fetch("http://127.0.0.1:8000/" + request.action, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: request.message }),
        })
            .then((response) => response.json())
            .then((response) => {
                sendResponse({ reply: response.reply });
            })
            .catch((error) => {
                sendResponse({ reply: "Error: " + error.message });
            });
    }

    if (request.action === "openpanel") {
        chrome.windows.create({
            url: chrome.runtime.getURL("sidebar.html"),
            type: "panel",
            width: 300,
            height: window.screen.availHeight,
            left: window.screen.availWidth - 300,
        });
    }

    return true;
});
