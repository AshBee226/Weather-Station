from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class MessageModel(BaseModel):
    message: str

@app.post("/sent")
async def message(messageContent: MessageModel):
    message = messageContent.message
    return {
        "msg": message
    }

@app.get("/request")
async def message():
    return {
        "msg": "message"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)