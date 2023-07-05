// on page load, send URL and body of tab to side panel
var url = window.location.href;
var body = document.body.innerHTML;
chrome.runtime.sendMessage({
    action: "sendPageInfo",
    pageInfo: {
        url: url,
        body: body,
    },
});
