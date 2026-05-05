from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.post("/sent")
async def message(data: dict = Body(...)):
    return {
        {data['msg']}
    }

@app.get("/request")
async def message():
    return {
        "msg": "message"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)