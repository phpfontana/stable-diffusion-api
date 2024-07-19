# stable-diffusion-api
Stable Diffusion API built with FastAPI, and Diffusers
Sure, here's an improved README for the Stable Diffusion API:

---

# Stable Diffusion API

Welcome to the Stable Diffusion API! This API leverages FastAPI and Diffusers to provide powerful image generation capabilities. Create stunning images from textual prompts using state-of-the-art diffusion models.

## Features

- **Image Generation**: Generate images from textual descriptions.
- **Base64 Encoding**: Receive images encoded in base64 format for easy integration.

## Endpoints

### Image Generation

`POST /api/generate`

Generate an image based on the provided textual prompt.

**Parameters**

- `model` (string): The model to use for image generation.
- `prompt` (string): The textual description to generate the image from.

**Example**

**Request**

```bash
curl -X 'POST' \
  'http://localhost:8000/api/generate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "stabilityai/sdxl-turbo",
    "prompt": "A beautiful landscape with a castle"
}'
```

**Response**

```json
{
  "image": ["iVBORw0KGgoAAAANSUhEUgAA..."]
}
```

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed.

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/phpfontana/stable-diffusion-api.git
   cd stable-diffusion-api
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

1. **Run the FastAPI server**

   ```bash
   fastapi run api/main.py --port 8000 --reload
   ```

2. **Access the API documentation**

   Open your browser and go to `http://localhost:8000/docs` to see the interactive API documentation.

## Usage

You can use the `/api/generate` endpoint to generate images based on textual prompts. The response will contain the image encoded in base64 format.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy using the Stable Diffusion API!

---

