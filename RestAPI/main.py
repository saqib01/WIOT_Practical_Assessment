from fastapi import FastAPI, Request
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

# ----------------------------
# MySQL DB Configuration
# ----------------------------
# Replace `mysql-service` with your MySQL service name in Kubernetes
#DATABASE_URL = "mysql+pymysql://dbuser:dbpassword@mysql-service:3306/logdb"
DATABASE_URL = "mysql+pymysql://root:mysql123@mysql-service.db.svc.cluster.local:3306/logdb"


engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ----------------------------
# Database Model
# ----------------------------
class LogEntry(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ip = Column(String(45), nullable=False)  # IPv6 safe
    timestamp = Column(DateTime, default=datetime.utcnow)


# Create tables if not exist
Base.metadata.create_all(bind=engine)


# ----------------------------
# API Routes
# ----------------------------
@app.post("/log-ip")
async def log_ip(request: Request):
    client_ip = request.client.host
    db = SessionLocal()

    log_entry = LogEntry(ip=client_ip)
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    db.close()

    return {
        "message": "IP logged successfully",
        "entry": {"ip": log_entry.ip, "timestamp": log_entry.timestamp.isoformat()}
    }


@app.get("/logs")
async def get_logs():
    db = SessionLocal()
    entries = db.query(LogEntry).all()
    db.close()

    return {
        "logs": [{"ip": e.ip, "timestamp": e.timestamp.isoformat()} for e in entries]
    }
