from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:alatj1030?@playlist-db.cd8siekmuj3l.ap-northeast-2.rds.amazonaws.com:5432/postgres"

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL)
# 세션 로컬 클래스 생성
SessionLocal = sessionmaker(autoflush=False, bind=engine)
# 베이스 모델 선언 (추후 모델 클래스 정의 시 사용)
Base = declarative_base()

# 데이터베이스 세션을 위한 의존성 주입 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()