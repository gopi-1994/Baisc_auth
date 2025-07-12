from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from typing import Annotated

app = FastAPI()

security = HTTPBasic()
username = "gopi"
password = "password"

@app.get("/")
async def baisc_auth():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)