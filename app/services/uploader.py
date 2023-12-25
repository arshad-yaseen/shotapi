import cloudinary.uploader
import base64
from fastapi import HTTPException

async def upload_to_cloudinary(screenshot, cloudinary_credentials):
    try:
        cloudinary.config(
            cloud_name=cloudinary_credentials['cloud_name'],
            api_key=cloudinary_credentials['api_key'],
            api_secret=cloudinary_credentials['api_secret'],
        )
        return cloudinary.uploader.upload(screenshot)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading to Cloudinary: {e}")

def convert_to_base64(screenshot):
    return base64.b64encode(screenshot).decode()
