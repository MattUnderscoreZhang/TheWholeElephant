chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "chat" || request.action === "sendpage") {
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
