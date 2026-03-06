from datetime import datetime

from fastapi import FastAPI
from app.models.telemetry import Telemetry
from app.db.database import engine, SessionLocal, Base
from app.models.db_models import TelemetryRecord
from app.models.alert_models import AlertRecord

app = FastAPI(title="IoT Data Pipeline", version="1.0.0")

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "IoT Data Pipeline Demo API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/telemetry")
def ingest_telemetry(payload: Telemetry):
    telemetry_data = payload.model_dump()

    if telemetry_data["timestamp"] is None:
        telemetry_data["timestamp"] = datetime.utcnow()

    db = SessionLocal()

    record = TelemetryRecord(
        device_id=telemetry_data["device_id"],
        temperature=telemetry_data["temperature"],
        humidity=telemetry_data["humidity"],
        status=telemetry_data["status"],
        timestamp=telemetry_data["timestamp"]
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    alerts_created = []

    if record.temperature > 35.0:
        alert = AlertRecord(
            device_id=record.device_id,
            alert_type="high_temperature",
            message="High temperature detected",
            temperature=record.temperature,
            humidity=record.humidity,
            status=record.status,
            timestamp=record.timestamp
        )
        db.add(alert)
        alerts_created.append("high_temperature")

    if record.humidity > 70.0:
        alert = AlertRecord(
            device_id=record.device_id,
            alert_type="high_humidity",
            message="High humidity detected",
            temperature=record.temperature,
            humidity=record.humidity,
            status=record.status,
            timestamp=record.timestamp
        )
        db.add(alert)
        alerts_created.append("high_humidity")

    if record.status.lower() == "warning":
        alert = AlertRecord(
            device_id=record.device_id,
            alert_type="warning_status",
            message="Device entered warning state",
            temperature=record.temperature,
            humidity=record.humidity,
            status=record.status,
            timestamp=record.timestamp
        )
        db.add(alert)
        alerts_created.append("warning_status")

    db.commit()
    db.close()

    return {
        "message": "Telemetry received and stored successfully",
        "record_id": record.id,
        "alerts_created": alerts_created,
        "data": {
            "device_id": record.device_id,
            "temperature": record.temperature,
            "humidity": record.humidity,
            "status": record.status,
            "timestamp": record.timestamp.isoformat()
        }
    }


@app.get("/telemetry")
def get_all_telemetry():
    db = SessionLocal()
    records = db.query(TelemetryRecord).all()
    db.close()

    return [
        {
            "id": record.id,
            "device_id": record.device_id,
            "temperature": record.temperature,
            "humidity": record.humidity,
            "status": record.status,
            "timestamp": record.timestamp.isoformat()
        }
        for record in records
    ]


@app.get("/telemetry/latest/{device_id}")
def get_latest_telemetry(device_id: str):
    db = SessionLocal()
    record = (
        db.query(TelemetryRecord)
        .filter(TelemetryRecord.device_id == device_id)
        .order_by(TelemetryRecord.timestamp.desc())
        .first()
    )
    db.close()

    if not record:
        return {"message": f"No telemetry found for device {device_id}"}

    return {
        "id": record.id,
        "device_id": record.device_id,
        "temperature": record.temperature,
        "humidity": record.humidity,
        "status": record.status,
        "timestamp": record.timestamp.isoformat()
    }


@app.get("/telemetry/history/{device_id}")
def get_device_history(device_id: str, limit: int = 10):
    db = SessionLocal()
    records = (
        db.query(TelemetryRecord)
        .filter(TelemetryRecord.device_id == device_id)
        .order_by(TelemetryRecord.timestamp.desc())
        .limit(limit)
        .all()
    )
    db.close()

    return [
        {
            "id": record.id,
            "device_id": record.device_id,
            "temperature": record.temperature,
            "humidity": record.humidity,
            "status": record.status,
            "timestamp": record.timestamp.isoformat()
        }
        for record in records
    ]


@app.get("/alerts")
def get_all_alerts():
    db = SessionLocal()
    alerts = db.query(AlertRecord).order_by(AlertRecord.timestamp.desc()).all()
    db.close()

    return [
        {
            "id": alert.id,
            "device_id": alert.device_id,
            "alert_type": alert.alert_type,
            "message": alert.message,
            "temperature": alert.temperature,
            "humidity": alert.humidity,
            "status": alert.status,
            "timestamp": alert.timestamp.isoformat()
        }
        for alert in alerts
    ]


@app.get("/alerts/{device_id}")
def get_device_alerts(device_id: str):
    db = SessionLocal()
    alerts = (
        db.query(AlertRecord)
        .filter(AlertRecord.device_id == device_id)
        .order_by(AlertRecord.timestamp.desc())
        .all()
    )
    db.close()

    return [
        {
            "id": alert.id,
            "device_id": alert.device_id,
            "alert_type": alert.alert_type,
            "message": alert.message,
            "temperature": alert.temperature,
            "humidity": alert.humidity,
            "status": alert.status,
            "timestamp": alert.timestamp.isoformat()
        }
        for alert in alerts
    ]