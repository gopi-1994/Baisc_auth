from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from typing import Annotated
import bcrypt


app = FastAPI()

security = HTTPBasic()
username = "gopi"
password = "password"
hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(hash)


@app.get("/")
async def basic_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username == username:
        password_check = bcrypt.checkpw(credentials.password.encode('utf-8'), hash)
        if password_check:    
            return {"message": "Welcome to the FastAPI application!"}
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password", headers={"WWW-Authenticate": "Basic"})
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials", headers={"WWW-Authenticate": "Basic"})

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)