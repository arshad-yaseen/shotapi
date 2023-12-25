from pydantic import BaseModel, Field, root_validator
from app.exceptions import MissingCloudinaryCredentialsError

class ScreenshotRequest(BaseModel):
    url: str
    type: str = Field(default='base64', pattern="^(base64|cloudinary)$")
    cloudinary_cloud_name: str = None
    cloudinary_api_key: str = None
    cloudinary_api_secret: str = None

    @root_validator(pre=True)
    # Check that the cloudinary credentials are present when the type is cloudinary
    def check_cloudinary_credentials(cls, values):
        if values.get('type') == 'cloudinary':
            cls.validate_cloudinary_credentials(values)
        return values

    @classmethod
    # Validate that the cloudinary credentials are present when the type is cloudinary
    def validate_cloudinary_credentials(cls, values):
        for field in ['cloudinary_cloud_name', 'cloudinary_api_key', 'cloudinary_api_secret']:
            if not values.get(field):
                raise MissingCloudinaryCredentialsError(field)