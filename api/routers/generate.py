from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from api.schemas.generate import *
from api.services.generate import *


router = APIRouter(
    prefix="/api/generate", tags=["generate"], responses={404: {"description": "Not found"}},
)

pipeline_kwargs = {
    "num_inference_steps": 5,
    "guidance_scale": 1,
    "height": 512,
    "width": 512,
}


@router.post("/", response_model=GenerateResponse)
async def main(request: GenerateRequest):
    try:
        image = generate_image(request.model, request.prompt, **pipeline_kwargs)
        base64_images = encode_image_to_base64(image)
        return GenerateResponse(image=[base64_images])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))