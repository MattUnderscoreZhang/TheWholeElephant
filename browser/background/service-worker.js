import {is_news_article_url} from "./is_news_article.js";


// side panel opens when icon is clicked
chrome.sidePanel
    .setPanelBehavior({ openPanelOnActionClick: true })
    .catch((error) => console.error(error));


// show README on installation
chrome.runtime.onInstalled.addListener(({reason}) => {
    if (reason !== "install") return;
    chrome.tabs.create({ url: "readme.html" });
});


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
