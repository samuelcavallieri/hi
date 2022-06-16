from tabnanny import check
from fastapi import FastAPI
from app.dto import RequestBody

app = FastAPI()

@app.get("/health-check", status_code=200) 
async def health_check():
    return "it works!" 

@app.post("/send", status_code=201) 
async def send(body: RequestBody):
    return {"message": body.message} 
