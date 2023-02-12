from fastapi import FastAPI
from .db import get_calls, create_call
from .models import CallInfo

app = FastAPI()


@app.get("/call-report")
def read_calls(phone: str):
    results = get_calls(phone)

    return {
        "success": True,
        "data": results,
    }


@app.post("/initiate-call")
def initiate_call(call_info: CallInfo):
    create_call(**dict(call_info))

    return {
        "success": True,
    }
