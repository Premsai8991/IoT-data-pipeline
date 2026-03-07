# IoT Data Pipeline Demo

A small but realistic **device-to-cloud IoT telemetry pipeline demo** built with **Python, FastAPI, SQLite, and a Python-based device simulator**.

This project demonstrates how IoT devices send telemetry data to a backend API, where it is validated, stored, processed, and monitored for alerts.

---

# IoT Data Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20Framework-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

A realistic **device-to-cloud IoT telemetry pipeline** built with FastAPI, SQLAlchemy, and SQLite.  
The system simulates IoT devices sending telemetry data, validates it, stores it in a database, and generates alerts for abnormal sensor readings.

# Features

- Simulated IoT device sending telemetry every **5 seconds**
- FastAPI **telemetry ingestion API**
- **Pydantic schema validation**
- **SQLite database storage using SQLAlchemy**
- Query APIs for **latest telemetry and historical data**
- **Rule-based alert generation**
- Alerts API for **device health monitoring**
- Interactive API documentation using **Swagger UI**

---

# Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Requests
- Uvicorn

---

## Project Architecture

```
Device Simulator
      ↓
FastAPI Telemetry API
      ↓
Schema Validation (Pydantic)
      ↓
Data Processing
      ↓
SQLite Database Storage
      ↓
Telemetry Query APIs
      ↓
Alert Detection System
      ↓
Alerts API
```

# Features

- Simulated IoT device sending telemetry every **5 seconds**
- **FastAPI REST API** for telemetry ingestion
- **Pydantic validation** for sensor data
- **SQLite database storage** using SQLAlchemy
- Query APIs for **latest telemetry and historical data**
- **Rule-based alert detection**
- Alerts API for **device monitoring**
- **Interactive Swagger API documentation**

---

# Tech Stack

| Technology | Purpose |
|-----------|--------|
| Python | Core programming language |
| FastAPI | High-performance API framework |
| SQLAlchemy | ORM for database access |
| SQLite | Lightweight telemetry database |
| Pydantic | Data validation |
| Requests | HTTP client for simulator |
| Uvicorn | ASGI server |

---

## Project Structure

```
iot-data-pipeline/
│
├── app/
│   ├── db/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── telemetry.py
│   │   ├── db_models.py
│   │   └── alert_models.py
│   │
│   └── main.py
│
├── simulator/
│   └── device_simulator.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

# API Endpoints

## Health Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | `/` | API status |
| GET | `/health` | Health check |

---

## Telemetry Endpoints

| Method | Endpoint | Description |
|------|------|------|
| POST | `/telemetry` | Ingest telemetry data |
| GET | `/telemetry` | Get all telemetry |
| GET | `/telemetry/latest/{device_id}` | Latest telemetry for device |
| GET | `/telemetry/history/{device_id}` | Telemetry history |

---

## Alerts Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | `/alerts` | Get all alerts |
| GET | `/alerts/{device_id}` | Get alerts for a specific device |

---

# Alert Detection Rules

The system automatically generates alerts when abnormal sensor values are detected.

| Condition | Alert Type |
|----------|-----------|
| Temperature > 35°C | High Temperature Alert |
| Humidity > 70% | High Humidity Alert |
| Device status = `"warning"` | Warning State Alert |

---

# Example Telemetry Payload

```json
{
  "device_id": "machine_001",
  "temperature": 34.5,
  "humidity": 62.1,
  "status": "running",
  "timestamp": null
}
```

# Example Alert Response

```json
{
  "id": 56,
  "device_id": "machine_001",
  "alert_type": "high_temperature",
  "message": "High temperature detected",
  "temperature": 35.8,
  "humidity": 56.48,
  "status": "running",
  "timestamp": "2026-03-06T18:36:27.879546"
}
```

---

### 1) Clone the repository

```bash
git clone https://github.com/Premsai8991/iot-data-pipeline-demo.git
cd iot-data-pipeline-demo
```

---

### 2) Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac / Linux**

```bash
source .venv/bin/activate
```

---

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4) Run the API server

```bash
python -m uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

### 5) Run the device simulator

Open a new terminal and run:

```bash
python simulator/device_simulator.py
```

The simulator will send telemetry data every **5 seconds**.

---

### 6) Test the API

Open the interactive API documentation:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all endpoints directly.

---

## Future Improvements

- Multi-device simulator
- Real-time telemetry dashboard
- Docker container support
- PostgreSQL database support
- MQTT ingestion pipeline
- Kafka streaming pipeline
- Data analytics and aggregation APIs

---

## Author

**Naga Prem Sai Nellure**

Florida Atlantic University  
M.S. Computer Engineering  

### Focus Areas

- Artificial Intelligence
- IoT Systems
- Cybersecurity
