from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()



@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)