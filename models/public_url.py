from pydantic import BaseModel


class VideoUrl(BaseModel):
    url: str
