// on request, send URL and body of tab
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "getPageInfo") {
        chrome.runtime.sendMessage({
            action: "sendPageInfo",
            pageInfo: {
                url: window.location.href,
                body: document.body.innerHTML,
            },
        });
    }
});
