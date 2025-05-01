from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Playlist(Base):
    __tablename__ = "playlist" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)        
    artist = Column(String, nullable=False)     
    added_date = Column(DateTime(timezone=True), server_default=func.now())
    audio_url = Column(String, nullable=False)

