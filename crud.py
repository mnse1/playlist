from sqlalchemy.orm import Session
from models import Playlist
from schemas import PlaylistCreate

def get_playlist(db: Session):
    return db.query(Playlist).all()

def create_playlist(db: Session, playlist: PlaylistCreate):
    new_song = Playlist(
        title=playlist.title,
        artist=playlist.artist,
        audio_url=playlist.audio_url
    )
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

def delete_playlist(db: Session, playlist_id: int):
    song = db.query(Playlist).filter(Playlist.id == playlist_id).first()
    if not song:
        return None 
    
    db.delete(song)
    db.commit()
    return song

def update_playlist(db: Session, playlist_id: int, playlist: PlaylistCreate):
    song = db.query(Playlist).filter(Playlist.id == playlist_id).first()
    if not song:
        return None

    song.title = playlist.title
    song.artist = playlist.artist

    db.commit()
    db.refresh(song)
    return song