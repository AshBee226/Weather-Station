import {
    tempThemes
} from "./tempThemes.js"

let message = document.getElementById("message")
let currentTemp = document.getElementsByClassName("currentTemp")
let body = document.getElementById("body")

let temperature = 0;
let time = "00:00:00"
let day = ""


function jsonConvert() {
    let data = {
        "msg": 1.0
    }
    fetch('http://192.168.1.94:8000/sent', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        "msg": 1.0 
    })
})
    .then(res => {
            return res.json()
        })

    .then(data => text.innerHTML = data.msg)


}


function changeText() {
    fetch("http://192.168.1.105:8000/get-data")
    .then(response => response.json())
    .then(data => {
    temperature = data.temp
    time = data.time
    day = data.day
    })
    console.log(temperature)
    console.log(time)
    console.log(day)

    for(var i=0; i<currentTemp.length; i++) {
        currentTemp[i].innerHTML = temperature + "°C"
    }

    Math.round(temperature)
    document.body.style.backgroundImage = tempThemes[temperature+5] 
    if (temperature >= 30) {
        document.body.style.backgroundColor = "rgb(243, 109, 0)"
    } else if (temperature <= -5) {
        document.body.style.backgroundColor = "rgb(69, 87, 247)"
    }
}



setInterval(changeText, 5000)
