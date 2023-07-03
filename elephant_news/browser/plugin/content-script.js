// send URL and HTML of tab to side panel

//window.onload = sendPageInfo;


//chrome.runtime.onMessage.addListener(function(request, sender) {
    //if (request.action == "getSource") {
        //this.pageSource = request.source;
        //var title = this.pageSource.match(/<title[^>]*>([^<]+)<\/title>/)[1];
        //alert(title)
    //}
//});


//chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    //chrome.tabs.executeScript(
        //tabs[0].id,
        //{ code: 'var s = document.documentElement.outerHTML; chrome.runtime.sendMessage({action: "getSource", source: s});' }
    //);
//});


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
    var doc = { url: url, title: title, body: body };
    sendResponse({ doc: doc });
    return true;
});
