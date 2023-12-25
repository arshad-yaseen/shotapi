from app.models.payload import ScreenshotRequest
from app.services.screenshot_taker import take_screenshot
from app.services.uploader import upload_to_cloudinary, convert_to_base64
from fastapi import HTTPException

async def process_screenshot(request: ScreenshotRequest):
    try:
        screenshot = await take_screenshot(request.url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error taking screenshot: {e}")

    # If the request type is base64, return the base64 encoded screenshot
    if request.type == "base64":
        return convert_to_base64(screenshot)
    # If the request type is cloudinary, upload the screenshot to Cloudinary and return the cloudinary response
    elif request.type == "cloudinary":
        cloudinary_credentials = {
            # The cloudinary credentials are passed in as part of the request
            'cloud_name': request.cloudinary_cloud_name,
            'api_key': request.cloudinary_api_key,
            'api_secret': request.cloudinary_api_secret
        }
        return await upload_to_cloudinary(screenshot, cloudinary_credentials)
