// src/components/AddSongForm.js
import React, { useState } from 'react';
import axios from 'axios';

const AddSongForm = ({ onSongAdded }) => {
  const [title, setTitle] = useState('');
  const [artist, setArtist] = useState('');
  const [audioUrl, setAudioUrl] = useState('');
  const [adminPW, setAdminPW] = useState('');
  const BASE_URL = 'http://13.125.75.235';  // EC2 퍼블릭 IP

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newSong = {
        title,
        artist,
        audio_url: audioUrl,
      };
      // 백엔드에 새로운 노래 추가 요청
      const response = await axios.post(`${BASE_URL}/playlist`, newSong, {
        headers: {
          'x-admin-secret': adminPW, // 서버에 설정한 비밀번호와 일치해야 함
        },
      });
      onSongAdded(response.data);
      console.log("버전 3");
      console.log("보내는 비밀번호:", adminPW);
      // 폼 초기화
      setTitle('');
      setArtist('');
      setAudioUrl('');
    } catch (error) {
      console.error('Error adding song:', error);
      alert("권한이 없습니다. 관리자만 추가할 수 있습니다.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
        required
      />
      <input
        type="text"
        value={artist}
        onChange={(e) => setArtist(e.target.value)}
        placeholder="Artist"
        required
      />
      <input
        type="text"
        value={audioUrl}
        onChange={(e) => setAudioUrl(e.target.value)}
        placeholder="YouTube URL"
        required
      />
      <input
        type="password"
        value={adminPW}
        onChange={(e) => setAdminPW(e.target.value)}
        placeholder="관리자 비밀번호" // 🔐 UI에 표시
        required
      />
      <button type="submit">Add</button>
    </form>
  );
};

export default AddSongForm;
