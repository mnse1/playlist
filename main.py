from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import crud
from typing import List
from schemas import PlaylistResponse

 
# uvicorn main:app --reload to run the server /playlist
# npm start to run the client   /playlist/client

#app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ADMIN_PW =  "admin1234"
Base.metadata.create_all(bind=engine)

# DB 세션을 의존성으로 주입받음
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

