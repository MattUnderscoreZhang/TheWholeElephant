chrome.browserAction.onClicked.addListener(function (tab) {
    chrome.tabs.create({ url: "popup.html" });
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "sendMessage") {
        fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: request.message })
        })
            .then(response => response.json())
            .then(data => {
                sendResponse({ reply: data.reply });
            })
            .catch(error => {
                console.error(error);
                sendResponse({ reply: "Error: " + error.message });
            });
    }

    return true;
});
