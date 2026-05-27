from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
app = FastAPI()

latest_message = ""
previous_message = ""

class Message(BaseModel):
    message: float

origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "http://192.168.1.94",
]

msgDB = mysql.connector.connect(
    host="192.168.1.94",
    port=3306,
    user="ashbee",
    password="1234",
    database = "recievedMessages"
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

    return {
        "msg": msg_body.message
        }

@app.get("/request")
async def message():
    return {
        "msg": "message"
    }

@app.get("/get-data")
async def getdata():
    global previous_message
    if latest_message != "" and latest_message != previous_message:
        sql = ( 
        "INSERT INTO recievedMessages (tempreture) " 
        "VALUES (%s)"
        )
        val = (latest_message,)
        cursor.execute(sql,val)

        msgDB.commit()
    
    previous_message = latest_message

    return {
        "data": latest_message
    }

    

#if __name__ == "__main__":
    #import uvicorn

    #uvicorn.run(app, host="192.168.1.105", port=8000)