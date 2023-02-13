from fastapi import FastAPI, status, HTTPException
from .db import get_calls, create_call
from .models import CallInfo

app = FastAPI()


@app.get("/call-report")
def read_calls(phone: str):
    try:
        results = get_calls(phone)

        return {
            "success": True,
            "data": results,
        }
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Couldn't process the request! Add something to table first!",
        )


@app.post("/initiate-call", status_code=status.HTTP_201_CREATED)
def initiate_call(call_info: CallInfo):
    try:
        create_call(**dict(call_info))
        return {
            "success": True,
        }
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Couldn't create the resource!",
        )
