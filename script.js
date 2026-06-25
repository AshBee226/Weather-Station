import {
    tempThemes
} from "./tempThemes.js"

let currentTemp = document.getElementsByClassName("currentTemp")
let currentDay = document.getElementById("currentDay")
let body = document.getElementById("body")

let temperature = [];
let time = "00:00:00"
let daysAround = ""


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
    fetch("http://192.168.1.94:8000/get-data")
    .then(response => response.json())
    .then(data => {
    temperature = data.temps
    time = data.time
    daysAround = data.daysAround
    })
    console.log(temperature)
    console.log(time)
    console.log(daysAround)

    document.getElementById("-3Days").innerHTML = daysAround[0]
    document.getElementById("-2Days").innerHTML = daysAround[1]
    document.getElementById("-1Days").innerHTML = daysAround[2]
    currentDay.innerHTML = "Today"
    document.getElementById("+1Days").innerHTML = daysAround[4]
    document.getElementById("+2Days").innerHTML = daysAround[5]
    document.getElementById("+3Days").innerHTML = daysAround[6]

    document.getElementById("-3Days_temp").innerHTML = temperature[0] + "°C"
    document.getElementById("-2Days_temp").innerHTML = temperature[1] + "°C"
    document.getElementById("-1Days_temp").innerHTML = temperature[2] + "°C"





    for(var i=0; i<currentTemp.length; i++) {
        currentTemp[i].innerHTML = temperature[3] + "°C"
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
