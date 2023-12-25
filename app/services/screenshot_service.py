from app.models.payload import ScreenshotRequest
from app.services.screenshot_taker import take_screenshot
from app.services.uploader import upload_to_cloudinary
from fastapi import HTTPException
import validators
from typing import Any


async def process_screenshot(request: ScreenshotRequest) -> Any:
    # Validate the URL
    validate_url(request.url)
    try:
        screenshot_base64 = await take_screenshot(request.url)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error taking screenshot: {e}"
        )

    # If the request type is base64, return the base64 encoded screenshot
    if request.type == "base64":
        return screenshot_base64
    # If the request type is cloudinary, upload the screenshot to Cloudinary and return the cloudinary response
    elif request.type == "cloudinary":
        cloudinary_credentials = {
            # The cloudinary credentials are passed in as part of the request
            "cloud_name": request.cloudinary_cloud_name,
            "api_key": request.cloudinary_api_key,
            "api_secret": request.cloudinary_api_secret,
        }
        return await upload_to_cloudinary(
            screenshot_base64=screenshot_base64,
            cloudinary_credentials=cloudinary_credentials,
        )


def validate_url(url: str):
    if not validators.url(url):
        raise HTTPException(status_code=400, detail=f"Invalid URL: {url}")
