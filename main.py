from fastapi import FastAPI
import psycopg2
import psycopg2.extras

app = FastAPI()


conn = psycopg2.connect(
 database="JIRA",
 user="postgres",
 password="ilyas13!A",
 host="127.0.0.1",
 port="5432")


@app.get("/")
def home():
    return {"sms": "Hello World yes"}



