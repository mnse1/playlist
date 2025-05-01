import React from 'react';
import YouTube from 'react-youtube';

const YouTubePlayer = ({ videoId, onEnd }) => {
  const opts = {
    height: '390',
    width: '640',
    playerVars: {
        autoplay: 1,
        origin: "http://playlist-frontend1.s3-website.ap-northeast-2.amazonaws.com"
    },
  };

  return <YouTube videoId={videoId} opts={opts} onEnd={onEnd}/>;
};


export default YouTubePlayer;   