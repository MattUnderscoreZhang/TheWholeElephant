// content.js
console.log('Whole Elephant Loading.');

//chrome.window.create({ url: 'https://www.google.com', state: 'minimized' });

//chrome.windows.create({
//    url: chrome.runtime.getURL('sidebar.html'),
//    type: 'panel',
//    width: 300,
//    height: window.screen.availHeight,
//    left: window.screen.availWidth - 300
//});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    //console.log('changing color');
    //if (request.color === "green") {
    //    document.body.style.backgroundColor = "green";
    //    sendResponse({ status: "done" });
    //}
    //return true;

    var url = window.location.href;
    var title = document.title;
    var body = document.documentElement.innerHTML;
    var doc = { 'url': url, 'title': title, 'body': body }
    sendResponse({ 'doc': doc });
    return true;
});

