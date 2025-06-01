# 음악 플레이리스트 관리 애플리케이션

FastAPI와 React를 이용한 음악 플레이리스트 관리 웹 애플리케이션
YouTube URL 기반으로 곡을 추가/삭제/수정/재생 가능 + 관리자 인증 기능

---

## 프로젝트 특징

- **곡 추가 (POST /playlist)**: 관리자 인증 필요
- **곡 삭제 (DELETE /playlist/{id})**: 관리자 인증 필요 
- **곡 수정 (PUT /playlist/{id})**
- **곡 목록 조회 (GET /playlist)**
- **YouTube URL 기반 곡 재생** (React YouTube Player)
- **관리자 인증**: 관리자만 곡 추가/삭제 가능
- **CORS 설정**: 프론트엔드와 백엔드 통신 지원

---

## 개발 환경

- FastAPI
- SQLAlchemy
- PostgreSQL (AWS RDS)
- React
- Axios
- YouTube React Player
- AWS EC2, S3

---

## 프로젝트 구조
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

## 배포 주소
http://playlist-frontend1.s3-website.ap-northeast-2.amazonaws.com/