from app.services.screenshot_taker import take_screenshot
from fastapi import HTTPException
import validators
from typing import Any
from fastapi.responses import StreamingResponse
from io import BytesIO


async def process_screenshot(
    url: str,
    format: str,
    width: int = None,
    height: int = None,
    full_page: bool = False,
    mobile: bool = False,
    dark_mode: bool = False,
    delay: int = 0,
    custom_js: str = None,
    user_agent: str = None,
) -> Any:
    # Validate the URL
    validate_url(url)
    try:
        screenshot = await take_screenshot(
            url,
            width,
            height,
            full_page,
            mobile,
            dark_mode,
            delay,
            custom_js,
            user_agent,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error taking screenshot: {e}"
        )

    # If the request format is base64, return the base64 encoded screenshot
    if format == "base64":
        return screenshot["base64"]
    # If the request format is png, return the png screenshot
    elif format == "png":
        return StreamingResponse(
            BytesIO(screenshot["png"]), media_type="image/png"
        )


def validate_url(url: str):
    if not validators.url(url):
        raise HTTPException(status_code=400, detail=f"Invalid URL: {url}")
