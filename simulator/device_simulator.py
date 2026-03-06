import time
import random
import requests

API_URL = "http://127.0.0.1:8000/telemetry"
DEVICE_ID = "machine_001"


def generate_telemetry():
    temperature = round(random.uniform(25.0, 40.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)

    if temperature > 36:
        status = "warning"
    else:
        status = "running"

    return {
        "device_id": DEVICE_ID,
        "temperature": temperature,
        "humidity": humidity,
        "status": status,
        "timestamp": None
    }


def send_telemetry():
    while True:
        payload = generate_telemetry()

        try:
            response = requests.post(API_URL, json=payload)

            print("Sent:", payload)
            print("Status Code:", response.status_code)

            try:
                print("Response:", response.json())
            except Exception:
                print("Raw Response:", response.text)

        except Exception as e:
            print("Error sending telemetry:", e)

        print("-" * 50)
        time.sleep(5)

if __name__ == "__main__":
    send_telemetry()