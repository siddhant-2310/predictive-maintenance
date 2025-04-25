import random
import json
from datetime import datetime, timedelta

def generate_sensor_data():
    # Generate current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Generate sensor readings
    sensor_data = {
        "timestamp": timestamp,
        "Type": random.choice([0, 1]),  # Machine Type
        "Air temperature [K]": round(random.uniform(295, 310), 2),
        "Process temperature [K]": round(random.uniform(305, 315), 2),
        "Rotational speed [rpm]": random.randint(1000, 3000),
        "Torque [Nm]": random.randint(10, 80),
        "Vibration Levels": random.randint(1, 10),
        "Operational Hours": random.randint(0, 10000),
        "RUL": random.randint(0, 100)  # Remaining Useful Life in days
    }
    return sensor_data

def generate_historical_data(days=30):
    """Generate historical data for the past N days"""
    data = []
    for i in range(days, 0, -1):
        record = generate_sensor_data()
        # Override timestamp with historical dates
        record['timestamp'] = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
        data.append(record)
    return data

if __name__ == "__main__":
    # Generate sample data
    current_data = generate_sensor_data()
    historical_data = generate_historical_data()
    
    # Print results
    print("Current Sensor Data:")
    print(json.dumps(current_data, indent=4))
    
    print("\nHistorical Data (Last 30 days):")
    print(json.dumps(historical_data, indent=4))
