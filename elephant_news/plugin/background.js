chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {

    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }, 
        body: JSON.stringify({ message: request.message })
    })
        .then(response => response.json())
        .then(response => {
            sendResponse({ reply: response.reply });
        })
        .catch(error => {
            sendResponse({ reply: "Error: " + error.message } );
        });

    return true;
});