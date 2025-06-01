http://playlist-frontend1.s3-website.ap-northeast-2.amazonaws.com/

YouTube URL을 통해 노래 등록, 재생 가능

React, FastAPI, PostgreSQL 기반
AWS EC2, S3, RDS 통해 배포
관리자 비밀번호 인증

기술 스택:
  backend:
    - FastAPI
    - SQLAlchemy
    - Pydantic
    - PostgreSQL (AWS RDS)
  frontend:
    - React
    - Axios
    - YouTube React Player
  deployment:
    - AWS EC2 (Backend)
    - AWS S3 (Frontend)
  others:
    - CORS
    - RESTful API 설계
    - 환경변수 (관리자 비밀번호)

features:
  - 곡 추가 (POST /playlist, 관리자 인증 필요)
  - 곡 삭제 (DELETE /playlist/{id}, 관리자 인증 필요)
  - 곡 수정 (PUT /playlist/{id})
  - 곡 목록 조회 (GET /playlist)
  - YouTube URL 기반 곡 재생 (React YouTube Player)
  - 관리자 인증 (x-admin-secret)
  - CORS 설정으로 프론트엔드와 백엔드 통신
  
프로젝트 구조조
  backend/
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    ├── schemas.py
  frontend/
    ├── src/
        ├── App.js
        ├── components/
            ├── AddSongForm.js
            ├── YouTubePlayer.js