import cloudinary.uploader
from fastapi import HTTPException


async def upload_to_cloudinary(
    screenshot_base64: str, cloudinary_credentials: dict
) -> dict:
    try:
        cloudinary.config(
            cloud_name=cloudinary_credentials["cloud_name"],
            api_key=cloudinary_credentials["api_key"],
            api_secret=cloudinary_credentials["api_secret"],
        )
        return cloudinary.uploader.upload(
            f"data:image/png;base64,{screenshot_base64}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error uploading to Cloudinary: {e}"
        )
