from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"messag": "Hello World yes"}