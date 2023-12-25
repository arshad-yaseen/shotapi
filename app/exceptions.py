class MissingCloudinaryCredentialsError(ValueError):
    def __init__(self, missing_field):
        message = f"{missing_field} is required when 'type' is 'cloudinary'"
        super().__init__(message)
