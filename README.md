http://playlist-frontend1.s3-website.ap-northeast-2.amazonaws.com/

YouTube URL을 통해 노래 등록, 재생 가능

React, FastAPI, PostgreSQL 기반
AWS EC2, S3, RDS 통해 배포
관리자 비밀번호 인증

기술 스택


  Backend: FastAPI, SQLAlchemy, PostgreSQL (AWS RDS)
  
  Frontend: React, Axios, YouTube React Player
  
  배포: AWS EC2 (백엔드), S3 정적 웹 호스팅 (프론트엔드)
  
  기타: CORS, Pydantic, RESTful API

기능


  백엔드 (FastAPI)
  곡 추가 (POST /playlist) - 관리자 인증 필요
  
  곡 삭제 (DELETE /playlist/{id}) - 관리자 인증 필요
  
  곡 수정 (PUT /playlist/{id})
  
  전체 곡 조회 (GET /playlist)
  
  프론트엔드 (React)
  곡 추가/삭제/재생 UI 제공
  
  YouTube URL 기반 플레이어
  
  관리자 비밀번호 입력 후 곡 추가/삭제 가능

  
