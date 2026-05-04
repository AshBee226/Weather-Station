let message = document.getElementById("message")
let JSONbtn = document.getElementById("JSONbtn")


JSONbtn.addEventListener("click", jsonConvert)

function jsonConvert() {
    let data = {
        "msg":message.value
    }
    console.log(JSON.stringify(data))

}


