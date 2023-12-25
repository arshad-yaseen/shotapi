from fastapi import APIRouter, HTTPException, Body
from app.models.payload import ScreenshotRequest
from app.services.screenshot_service import process_screenshot

router = APIRouter()

@router.get("/")
async def root():
    return 'Hello from the screenshot service!'

@router.post("/")
async def get_screenshot(request: ScreenshotRequest = Body(...)):
    try:
        return await process_screenshot(request)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
