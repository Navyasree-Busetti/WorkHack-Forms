network = {
    baseUrl: "http://localhost:8000",
    makeHttpRequest: function (url, method, data) {
        return new Promise(function(res, rej){ 
            var xhr = new XMLHttpRequest();
            xhr.open(method, url, true);
            xhr.send(data);
            xhr.onreadystatechange = function(){
                if(xhr.readyState === 4){
                    if(xhr.status.toString()[0] === "2" || xhr.status.toString()[0] === "3"){
                        return res(xhr);
                    }
                    else{
                        return rej(xhr);
                    }
                }
            }
        })
    }
}