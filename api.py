from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
app = FastAPI()

latest_message = 9

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

def findTemps(date):
    temps = []
    total = 0
    for i in range(1,4):
        date = date
        sql_temp_3before_final = None
        total = 0


        sql_3before_statement = "SELECT DATE_SUB(%s, INTERVAL %s DAY)"
        data = (date, i)
        cursor.execute(sql_3before_statement, data)
        
        sql_temp_3before = "SELECT temperature FROM recievedMessages WHERE date = %s ORDER BY id DESC"
        date3 = cursor.fetchone()
        cursor.execute(sql_temp_3before, date3)
        sql_temp_3before = cursor.fetchall()       

        for i in range(len(sql_temp_3before)):
            total = total + int(sql_temp_3before[i][0])

        sql_temp_3before_final = total // len(sql_temp_3before)
    
        temps.append(sql_temp_3before_final)
        
    return temps

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

    if day == "Monday":
        temp = findTemps(date[0])
    elif day == "Tuesday":
        daysAround = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
        temp = findTemps(date[0])

    elif day == "Wednesday":
        daysAround = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        temp = findTemps(date[0])

    elif day == "Thursday":
        daysAround = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        temp = findTemps(date[0])

    elif day == "Friday":
        daysAround = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]
        temp = findTemps(date[0])

    elif day == "Saturday":
        daysAround = ["Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday"]
        temp = findTemps(date[0])

    elif day == "Sunday":
        daysAround = ["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
        temp = findTemps(date[0])

    temp.append(latest_message)

        

    return {
        "temps": temp,
        "time": time,
        "daysAround": daysAround
    }




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.1.216", port=8000)






