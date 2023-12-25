from fastapi import FastAPI
from app.api.endpoints import screenshot

app = FastAPI()

# Include the routers from different endpoints
app.include_router(screenshot.router)
