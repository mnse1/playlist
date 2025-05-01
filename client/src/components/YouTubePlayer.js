import React from 'react';
import YouTube from 'react-youtube';

const YouTubePlayer = ({ videoId, onEnd }) => {
  const opts = {
    height: '390',
    width: '640',
    playerVars: {
        autoplay: 1,
        origin: "http://localhost:3000" // YouTube CORS 문제 방지
    },
  };

  return <YouTube videoId={videoId} opts={opts} onEnd={onEnd}/>;
};


export default YouTubePlayer;   