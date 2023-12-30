from fastapi import FastAPI, HTTPException, Body, Request
from app.models.payload import ScreenshotRequest
from app.services.screenshot_service import process_screenshot
from app.core.rate_limiter import check_rate_limit

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello from ShotAPI!",
        "documentation": "https://github.com/arshad-yaseen/shotapi/blob/main/README.md",
    }


@app.post("/")
async def get_screenshot(
    request: Request, screenshot_request: ScreenshotRequest = Body(...)
):
    client_ip = request.client.host
    # Rate limit is set at 10 requests per minute
    rate_per_minute = 10
    check_rate_limit(client_ip, rate_per_minute)

    try:
        return await process_screenshot(screenshot_request)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
