# ShotAPI

ShotAPI is a fast and reliable screenshot capture API, built on top of Selenium. It allows users to easily capture screenshots of web pages and retrieve them in various formats. 

## Features

- Capture screenshots of web pages.
- Customize the format of the screenshot.
- Support for full-page captures.
- Mobile view and dark mode options.
- Execute custom JavaScript code.
- Specify the user agent.
- Introduce a delay before capturing.

## Using the API

To capture a screenshot, send a `GET` request to the API's endpoint:

```bash
GET http://localhost:3000/take
```
### Request Parameters

| Parameter          | Description                                                 | Required | Default |
|--------------------|-------------------------------------------------------------|----------|---------|
| `url`              | URL of the web page to capture                              | Yes      | -       |
| `format`           | Screenshot format (`base64` or `png`)                       | No       | `base64` |
| `width`            | Width of the browser window (in pixels)                     | No       | 1280       |
| `height`           | Height of the browser window (in pixels)                    | No       | 800       |
| `full_page`        | Capture the full page (true or false)                       | No       | false   |
| `mobile`           | Enable mobile view (true or false)                          | No       | false   |
| `dark_mode`        | Enable dark mode (true or false)                            | No       | false   |
| `delay`            | Delay before capturing the screenshot (in seconds)          | No       | 0       |
| `custom_js`        | Custom JavaScript code to execute on the page              | No       | -       |
| `user_agent`       | Specify the User-Agent header for the request              | No       | -       |


### Example Requests

Capture normal screenshot:

```bash
curl "http://localhost:3000/take?url=https://stripe.com&format=png" -o screenshot.png
```

Capture a Full-Page Screenshot in PNG Format:

```bash
curl "http://localhost:3000/take?url=https://github.com&format=png&full_page=true" -o screenshot.png
```

Capture a Screenshot of the Mobile View:

```bash
curl "http://localhost:3000/take?url=https://vercel.com&format=png&mobile=true" -o screenshot.png
```

### Response

The API will return the screenshot either as a base64 encoded string or as a PNG image, depending on the specified format.

### Rate Limiting

The API is rate limited to 10 requests per minute per IP address. If you exceed this limit, you will receive a `429 Too Many Requests` response.

## Error Handling

The API uses standard HTTP response codes to indicate the success or failure of requests. In case of an error, the response includes a descriptive message.

## Development and Contributions

Contributions to ShotAPI are welcome. For guidelines on contributing, Please read the [contributing guide](/CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/arshad-yaseen/shotapi?tab=MIT-1-ov-file) file for details.
