function build_from_github(name, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", "https://api.github.com/users/" + name, true); // true for asynchronous 
    xmlHttp.send(null);
}


document.addEventListener("DOMContentLoaded", function(event) {
    
    document.getElementsByName("from").forEach(function(el) {
        let who = el.getAttribute("attr");
        // let when = el.getAttribute("attr-when");

        build_from_github(who, function(result) {
            let json = JSON.parse(result);

            let img = document.createElement('img');
            img.className = "from-img";
            img.src = json.avatar_url;
            el.appendChild(img);

            let span = document.createElement('span');
            span.textContent = " by "
            span.className = "italic-grey"
            el.appendChild(span);

            let a = document.createElement('a')
            a.href = json.html_url;
            a.innerText = json.name;
            el.appendChild(a);

            span = document.createElement('span');
            span.textContent = " at "
            span.className = "italic-grey"
            el.appendChild(span);
// date formatting
        });
    });

});