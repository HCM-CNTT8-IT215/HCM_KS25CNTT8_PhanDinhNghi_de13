from fastapi import FastAPI
from pydantic import BaseModel
# from model import Patients
# from database import base



app = FastAPI()

# Base_database_all(bind=engine)

@app.get("/patients")
def get_patient():
    return{
        "message": "hello"
    }


    