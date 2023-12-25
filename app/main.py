from fastapi import FastAPI
from app.api.endpoints import take
from fastapi import APIRouter

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'Hello from ShotAPI!'}

app.include_router(take.router)
