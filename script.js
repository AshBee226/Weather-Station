let message = document.getElementById("message")
let JSONbtn = document.getElementById("JSONbtn")


JSONbtn.addEventListener("click", jsonConvert)

function jsonConvert() {
    let data = {
        "msg":message.value
    }
    fetch('http://127.0.0.1:8000/sent', {
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
    .then(data => console.log(data))

}

