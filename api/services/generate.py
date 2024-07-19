from typing import List
from io import BytesIO
from PIL import Image
import base64
from diffusers import DiffusionPipeline
import torch

def generate_image(model: str, prompt: str, **pipeline_kwargs):
    pipe = DiffusionPipeline.from_pretrained(model, torch_dtype=torch.float16, variant="fp16").to("mps")
    image = pipe(prompt=prompt, **pipeline_kwargs).images[0]
    return image

def encode_image_to_base64(image: Image.Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()