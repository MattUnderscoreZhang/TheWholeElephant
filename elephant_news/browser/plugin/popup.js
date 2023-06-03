//document.querySelector("#sendButton").addEventListener("click", function () {
//    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//        if (tabs[0].url?.startsWith("chrome://")) return undefined;
//        var tabId = tabs[0].id;
//        chrome.scripting.executeScript({
//            target: { tabId: tabId },
//            function: function () {
//                var innerHTML = document.documentElement.innerHTML;
//                chrome.runtime.sendMessage({ action: "sendInnerHTML", innerHTML: innerHTML });
//            }
//        });
//    });
//});


//console.log('popup');
//document.getElementById("sendButton").addEventListener("click", function (event) {
//    event.preventDefault();

//    var message = document.getElementById("message").value;


//    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//        // skip urls like "chrome://" to avoid extension error
//        if (tabs[0].url?.startsWith("chrome://")) return undefined;

//        console.log(tabs[0].title);
//        console.log(tabs[0].url);

//        var tabId = tabs[0].id;
//        chrome.scripting.executeScript({
//            target: { tabId: tabId },
//            function: function () {
//                var innerHTML = document.documentElement.innerHTML;
//                chrome.runtime.sendMessage({ action: "sendInnerHTML", innerHTML: innerHTML });
//            }
//        });
//    });


//    //var text = document.body.innerHTML //.replace(/<\/?[^>]+(>|$)/g, "");


//    //chrome.runtime.sendMessage({ action: "sendMessage", message: message }, function (response) {
//    //    if (response.success) {
//    //        console.log("Message sent successfully");
//    //    } else {
//    //        console.log("Error sending message");
//    //    }
//    //});
//});



document.addEventListener("DOMContentLoaded", function () {
    const messageContainer = document.getElementById("message-container");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-btn");

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
         chrome.runtime.sendMessage({ action: "sendMessage", message }, function (response) {
             if (response) {
               // alert(JSON.stringify(response))
                messageContainer.innerHTML += `<p><strong>Server response:</strong> ${response.reply}</p>`;
            }
        });
    }

});

// https://stackoverflow.com/questions/19758028/chrome-extension-get-dom-content