// content.js
console.log('Hello, content!');
chrome.tabs.executeScript(null, {
    file: "content.js"
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action == "getTextContent") {
        var url = window.location.href;
        var text = document.body.innerText.replace(/<\/?[^>]+(>|$)/g, "");
        text = text.replace(/\s+/g, " ").trim();
        sendResponse({ url: url, content: text });
        return true;
    }
});