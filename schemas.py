from pydantic import BaseModel
from datetime import datetime

class PlaylistCreate(BaseModel):
    title: str
    artist: str
    audio_url: str

class PlaylistResponse(BaseModel):
    id: int
    title: str
    artist: str
    added_date: datetime
    audio_url: str

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")
        }
