# Temporary Image Upload API

This API service allows users to upload, retrieve, and delete images temporarily. Uploaded images are stored for a duration of 5 minutes before being automatically deleted.

## Features

- **Image Upload**: Users can upload images to the server.
- **Retrieve Image**: Users can retrieve uploaded images using their IDs.
- **Delete Image**: Users can delete uploaded images using their IDs.
- **Temporary Storage**: Uploaded images are stored temporarily for 5 minutes.
- **Automatic Cleanup**: An automated process deletes expired images from the server.

## Endpoints

### Upload Image

- **URL:** `/api/upload`
- **Method:** POST
- **Request Parameters:**
  - `image`: The image file to be uploaded.

#### Example

```python
import requests

url = 'https://your-vercel-app-url/api/upload'
files = {'image': open('example_image.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

#### Response

```json
{
    "image_id": "1630303963"
}
```

### Retrieve Image

- **URL:** `/api/image/<image_id>`
- **Method:** GET
- **Request Parameters:**
  - `<image_id>`: The ID of the image to be retrieved.

#### Example

```python
import requests

image_id = '1630303963'
url = f'https://your-vercel-app-url/api/image/{image_id}'
response = requests.get(url)
with open('downloaded_image.jpg', 'wb') as f:
    f.write(response.content)
```

#### Response

If the image exists and has not expired, the response will be the image file. If the image does not exist or has expired, the response will be:

```json
{
    "error": "Image not found or expired"
}
```

### Delete Image

- **URL:** `/api/delete/<image_id>`
- **Method:** DELETE
- **Request Parameters:**
  - `<image_id>`: The ID of the image to be deleted.

#### Example

```python
import requests

image_id = '1630303963'
url = f'https://your-vercel-app-url/api/delete/{image_id}'
response = requests.delete(url)
print(response.json())
```

#### Response

```json
{
    "message": "Image deleted successfully"
}
```

## Usage

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Deploy your Flask application to Vercel.
3. Use the provided endpoints to upload, retrieve, and delete images.

## Notes

- This API service is intended for temporary image storage only.
- Images are automatically deleted after 5 minutes.
