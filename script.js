let message = document.getElementById("message")
let JSONbtn = document.getElementById("JSONbtn")
let text = document.getElementById("text")


JSONbtn.addEventListener("click", jsonConvert)

function jsonConvert() {
    let data = {
        "msg":message.value
    }
    fetch('http://192.168.1.94:8000/sent', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        message: message.value
    })
})
    .then(res => {
            return res.json()
        })

    .then(data => text.innerHTML = data.msg)

    console.log(data)

}

//127.0.0.1

//http://192.168.1.94:8000/sent