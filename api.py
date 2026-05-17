from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

latest_message = ""

class Message(BaseModel):
    message: str

origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "http://192.168.1.94",
]

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
    return {
        "data": latest_message
    }

#if __name__ == "__main__":
    #import uvicorn

    #uvicorn.run(app, host="192.168.1.76", port=8000)

