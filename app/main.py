from fastapi import FastAPI, HTTPException, Query, Request
from app.services.screenshot_service import process_screenshot
from app.core.rate_limiter import check_rate_limit

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello from ShotAPI!",
        "documentation": "https://github.com/arshad-yaseen/shotapi/blob/main/README.md",
    }


@app.get("/take")
async def get_screenshot(
    request: Request,
    url: str = Query(..., description="The URL to take a screenshot of"),
    format: str = Query(
        "base64", description="The format of the screenshot (base64 or png)"
    ),
    width: int = Query(1280, description="Width of the screenshot (optional)"),
    height: int = Query(
        800, description="Height of the screenshot (optional)"
    ),
    full_page: bool = Query(
        False, description="Capture full page (default: False)"
    ),
    mobile: bool = Query(
        False, description="Capture mobile view (default: False)"
    ),
    dark_mode: bool = Query(
        False, description="Enable dark mode (default: False)"
    ),
    delay: int = Query(
        0,
        description="Delay in seconds before taking the screenshot (default: 0)",
    ),
    custom_js: str = Query(
        None, description="Custom JavaScript to execute on the page (optional)"
    ),
    user_agent: str = Query(
        None, description="Custom User-Agent header (optional)"
    ),
):
    client_ip = request.client.host
    rate_per_minute = 10  # 10 requests per minute per IP
    check_rate_limit(client_ip, rate_per_minute)

    try:
        return await process_screenshot(
            url,
            format,
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
            status_code=e.status_code if hasattr(e, "status_code") else 500,
            detail=f"Error processing screenshot: {str(e)}",
        )
