from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
app = FastAPI()

latest_message = 5

class Message(BaseModel):
    message: float

origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "http://192.168.1.94",
]

days_of_the_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


msgDB = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database = "messages"
)


cursor = msgDB.cursor(buffered=True)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sent")
async def post_message(msg_body: Message):
    global latest_message

    latest_message = msg_body.message

    if latest_message != "":
        sql = ( 
        "INSERT INTO recievedMessages (tempreture, date, time) " 
        "VALUES (%s,CURDATE(), CURTIME())"
        )
        val = (latest_message,)
        cursor.execute(sql,val)

        msgDB.commit()

    return {
        "msg": msg_body.message
        }

@app.get("/get-data")
async def getdata():

    sql_time = "SELECT time FROM recievedMessages WHERE temperature = %s ORDER BY id DESC"
    temp = (latest_message,)

    cursor.execute(sql_time, temp)

    time = cursor.fetchone()
    time = time[0]

    sql_date = "SELECT date FROM recievedMessages WHERE temperature = %s ORDER BY id DESC"
    cursor.execute(sql_date, temp)

    date = cursor.fetchone()

    sql_day = ("SELECT WEEKDAY(%s)")
    date = (date[0],)
    cursor.execute(sql_day,date)
    
    day_num = cursor.fetchone()[0]
    day = days_of_the_week[day_num]
    print(day)
        

    return {
        "temp": int(latest_message),
        "time": time,
        "day": day
    }




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.1.105", port=8000)
