from typing import List
from pydantic import BaseModel

class GenerateRequest(BaseModel):
    model: str
    prompt: str

class GenerateResponse(BaseModel):
    image: List[str]

""""
example:
{
    "model": "stabilityai/sdxl-turbo",
    "prompt": "A beautiful landscape with a castle"
}

"""