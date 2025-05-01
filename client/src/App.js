// src/App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import AddSongForm from './components/AddSongForm';
import YouTubePlayer from './components/YouTubePlayer';
import './App.css';

const App = () => {
  const [playlist, setPlaylist] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const BASE_URL = 'http://13.125.75.235';  // EC2 퍼블릭 IP

  const fetchPlaylist = async () => {
    try {
      const response = await axios.get(`${BASE_URL}/playlist`);
      setPlaylist(Array.isArray(response.data) ? response.data : []);
    } catch (error) {
      console.error('Error fetching playlist:', error);
    }
  };

  useEffect(() => {
    fetchPlaylist();
  }, []);

  const currentSong = playlist[currentIndex];
  const extractVideoId = (url) => {
    if (!url) return null;
    const match = url.match(/(?:youtube\.com\/(?:.*v=|.*\/)|youtu\.be\/)([0-9A-Za-z_-]{11})/);
    return match ? match[1] : null;
  };

  const handleEnd = () => {
    if (currentIndex + 1 < playlist.length) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  return (
    <div>
      <h1>Playlist</h1>
      <AddSongForm onSongAdded={fetchPlaylist} />
      <h2>list</h2>
      <ul>
      {Array.isArray(playlist) && playlist.length > 0 ? (
    playlist.map((song, idx) => (
      <li key={song.id}>
        <strong>{song.title}</strong> - {song.artist}
        <button onClick={() => setCurrentIndex(idx)}>재생</button>
        <button onClick={() => {
          const adminPW = prompt("관리자 비밀번호를 입력하세요");
          if (!adminPW) return;

          axios.delete(`${BASE_URL}/playlist/${song.id}`, {
            headers: {
              'x-admin-secret': adminPW,
            }
          })
          .then(fetchPlaylist)
          .catch((error) => {
            alert("삭제 실패: 관리자만 삭제할 수 있습니다.");
            console.error("삭제 오류:", error);
          });
        }}>
          삭제
        </button>
      </li>
    ))
  ) : (
    <li>플레이리스트가 없습니다.</li>
  )}
        {playlist.map((song, idx) => (
          <li key={song.id}>
            <strong>{song.title}</strong> - {song.artist}
            <button onClick={() => setCurrentIndex(idx)}>재생</button>
            <button onClick={() => {
              const adminPW = prompt("관리자 비밀번호를 입력하세요");
              if (!adminPW) return;

              axios.delete(`${BASE_URL}/playlist/${song.id}`, {
                headers: {
                  'x-admin-secret': adminPW,
                }
              })
              .then(fetchPlaylist)
              .catch((error) => {
                alert("삭제 실패: 관리자만 삭제할 수 있습니다.");
                console.error("삭제 오류:", error);
              });
            }}>
              삭제
            </button>
          </li>
        ))}
      </ul>
      {currentSong && (
        <p style={{ textAlign: "center", fontWeight: "bold" }}>
          🎵 현재 재생 중: {currentSong.title} - {currentSong.artist}
        </p>
      )}
      {currentSong && (
        <div>
          <YouTubePlayer videoId={extractVideoId(currentSong.audio_url)} onEnd={handleEnd} />
        </div>
      )}
    </div>
  );
};

export default App;