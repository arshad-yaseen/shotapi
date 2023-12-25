from pydantic import BaseModel, Field, root_validator
from app.exceptions import MissingCloudinaryCredentialsError
from typing import Optional


class ScreenshotRequest(BaseModel):
    url: str
    format: str = Field(default="base64", pattern="^(base64|cloudinary_url)$")
    cloudinary_cloud_name: Optional[str] = None
    cloudinary_api_key: Optional[str] = None
    cloudinary_api_secret: Optional[str] = None

    @root_validator(pre=True)
    # Check that the cloudinary credentials are present when the format is cloudinary
    def check_cloudinary_credentials(cls, values):
        if values.get("format") == "cloudinary_url":
            cls.validate_cloudinary_credentials(values)
        return values

    @classmethod
    # Validate that the cloudinary credentials are present when the format is cloudinary
    def validate_cloudinary_credentials(cls, values):
        for field in [
            "cloudinary_cloud_name",
            "cloudinary_api_key",
            "cloudinary_api_secret",
        ]:
            if not values.get(field):
                raise MissingCloudinaryCredentialsError(field)
