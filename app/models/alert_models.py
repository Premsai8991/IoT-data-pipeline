from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class AlertRecord(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True, nullable=False)
    alert_type = Column(String, nullable=False)
    message = Column(String, nullable=False)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    status = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)