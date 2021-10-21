import config.configs as cf
from common.minio import MinioModel
from services.fraud_service import FraudDetection
from init import SessionLocal

fraudDetection = FraudDetection()
UserSession = dict()
SessionMap = dict()
ListAuth = dict()
ListAction = list()

def get_db():
    db = SessionLocal()
    try:
        yield db
    
    finally:
        db.close()