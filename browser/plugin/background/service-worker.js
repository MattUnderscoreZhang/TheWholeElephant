// side panel opens when icon is clicked
chrome.sidePanel
    .setPanelBehavior({ openPanelOnActionClick: true })
    .catch((error) => console.error(error));


// show README on installation
chrome.runtime.onInstalled.addListener(({reason}) => {
    if (reason !== "install") return;
    chrome.tabs.create({ url: "readme.html" });
});


// function to check if URL is a news article
function is_news_article_url(url) {
    const news_urls = [  // RegExp objects
        /^https:\/\/www\.foxnews\.com\/(?!opinion\/)[^\/]+\/[^\/]+\/?.*$/
    ]
    return news_urls.some((re) => re.test(url.href));
}


// side panel changes if the user is looking at a news article
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


// sends data to backend server
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "sendPageInfo") {
        fetch("http://127.0.0.1:8000/analyze_page", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify( request.pageInfo ),
        })
            .then((response) => response.json())
            .then((response) => {
                sendResponse({ reply: response.reply });
            })
            .catch((error) => {
                sendResponse({ reply: "Error: " + error.message });
            });
    }
    return true;  // runs sendResponse asynchronously
});
