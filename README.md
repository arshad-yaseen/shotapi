# ShotAPI

ShotAPI is a fast and reliable screenshot capture API, built on top of Selenium. It allows users to easily capture screenshots of web pages and retrieve them in various formats. 

## Features

- Capture full-page screenshots of web pages.
- Simple and intuitive REST API interface.
- Supports returning screenshots in different formats.

## Using the API

To capture a screenshot, send a `POST` request to the API's endpoint.

```bash
POST https://shotapi.arshadyaseen.com
```
### Request Body Parameters

| Parameter | Description                              | Required | Default |
|-----------|------------------------------------------|----------|---------|
| `url`     | Web page URL to screenshot               | Yes      | -       |
| `format`  | Screenshot format (`base64` or `cloudinary_url`) | No       | `base64` |

For `cloudinary_url` format, additional parameters are required:
- `cloudinary_cloud_name`: Your Cloudinary cloud name.
- `cloudinary_api_key`: Your Cloudinary API key.
- `cloudinary_api_secret`: Your Cloudinary API secret.

### Example Requests

Using `base64` format:

```bash
curl -X 'POST' \
  'https://shotapi.arshadyaseen.com' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://example.com", "format": "base64"}'
```

Using `cloudinary_url` format:

```bash
curl -X 'POST' \
  'https://shotapi.arshadyaseen.com' \
  -H 'Content-Type: application/json' \
  -d '{
        "url": "https://example.com",
        "format": "cloudinary_url",
        "cloudinary_cloud_name": "your_cloud_name",
        "cloudinary_api_key": "your_api_key",
        "cloudinary_api_secret": "your_api_secret"
      }'
```

### Response

The API will return the screenshot as a base64 encoded string or a standard Cloudinary response including secure_url, depending on the specified format.

## Error Handling

The API uses standard HTTP response codes to indicate the success or failure of requests. In case of an error, the response includes a descriptive message.

## Development and Contributions

Contributions to ShotAPI are welcome. For guidelines on contributing, Please read the [contributing guide](/CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/arshad-yaseen/shotapi?tab=MIT-1-ov-file) file for details.