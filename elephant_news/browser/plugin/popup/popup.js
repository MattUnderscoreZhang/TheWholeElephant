const messageContainer = document.getElementById("chatbox--message-container");
const userInput = document.getElementById("chatbox--user-input");
const sendButton = document.getElementById("chatbox--send-btn");
const analyzeButton = document.getElementById("chatbox--analyze-btn");

analyzeButton.onclick = async function (e) {
    let queryOptions = { active: true, currentWindow: true };
    await chrome.tabs.query(
        { active: true, currentWindow: true },
        function (tabs) {
            chrome.tabs.sendMessage(
                tabs[0].id,
                { color: "green" },
                function (doc) {
                    chrome.runtime.sendMessage(
                        { action: "sendpage", message: doc["doc"] },
                        function (response) {
                            if (response) {
                                // alert(JSON.stringify(response));
                                messageContainer.innerHTML += `<p><strong>Server response:</strong> ${response.reply}</p>`;
                            }
                        }
                    );
                }
            );
        }
    );
};

document.addEventListener("DOMContentLoaded", function () {
    sendButton.addEventListener("click", function () {
        const message = userInput.value.trim();
        //var message = document.documentElement.innerHTML;
        if (message !== "") {
            messageContainer.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
            userInput.value = "";
            sendMessage(message);
        }
    });

    userInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            sendButton.click();
        }
    });

    function sendMessage(message) {
        chrome.runtime.sendMessage({ action: "openpanel" });
        chrome.runtime.sendMessage(
            { action: "chat", message },
            function (response) {
                if (response) {
                    // alert(JSON.stringify(response))
                    messageContainer.innerHTML += `<p><strong>Server response:</strong> ${response.reply}</p>`;
                }
            }
        );
    }
});

// https://stackoverflow.com/questions/19758028/chrome-extension-get-dom-content
