from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import crud
from typing import List
from schemas import PlaylistResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["https://playlist-frontend1.s3-website.ap-northeast-2.amazonaws.com"],
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ADMIN_PW =  "admin1234"
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Hello, World!"}

@app.get("/playlist", response_model=List[PlaylistResponse])
def read_playlist(db: Session = Depends(get_db)):
    return crud.get_playlist(db)

@app.post("/playlist")
def create_playlist(
    playlist: crud.PlaylistCreate,
    db: Session = Depends(get_db),
    x_admin_secret: str = Header(...)
):
    if x_admin_secret != ADMIN_PW:
        raise HTTPException(status_code=403, detail="Forbidden")
    return crud.create_playlist(db, playlist)

@app.delete("/playlist/{playlist_id}", response_model=PlaylistResponse)
def remove_song(playlist_id: int,
    db: Session = Depends(get_db),
    x_admin_secret: str = Header(...)):
    if x_admin_secret != ADMIN_PW:
        raise HTTPException(status_code=403, detail="Forbidden")

    deleted_song = crud.delete_playlist(db, playlist_id)
    if not deleted_song:
        raise HTTPException(status_code=404, detail="Song not found")
    return deleted_song

@app.put("/playlist/{playlist_id}", response_model=PlaylistResponse)
def update_song(playlist_id: int, playlist: crud.PlaylistCreate, db: Session = Depends(get_db)):
    updated_song = crud.update_playlist(db, playlist_id, playlist)
    if not updated_song:
        raise HTTPException(status_code=404, detail="Song not found")    
    return updated_song

