// on side panel load, get URL and body from tab
chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var tabId = tabs[0].id;
    chrome.tabs.sendMessage(
        tabId, { action: "getPageInfo" }
    );
});


// get page info and send to backend server for analysis
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "sendPageInfo") {
        fetch("http://127.0.0.1:8000/analyze_page", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify( message.pageInfo ),
        })
            .then((response) => response.json())
            .then((response) => {
                document.body.querySelector('#analysis').innerText = response;
            })
            .catch((error) => {
                document.body.querySelector('#analysis').innerText = "Error: " + error.message;
            });
    }
    return true;  // runs sendResponse asynchronously
});
