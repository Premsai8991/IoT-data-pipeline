from pydantic import BaseModel
from datetime import datetime


class Telemetry(BaseModel):
    device_id: str
    temperature: float
    humidity: float
    status: str
    timestamp: datetime | None = None