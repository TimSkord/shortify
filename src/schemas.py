from pydantic import BaseModel


class URLCreate(BaseModel):
    full_url: str


class URLResponse(BaseModel):
    id: int
    short_url: str
    full_url: str
