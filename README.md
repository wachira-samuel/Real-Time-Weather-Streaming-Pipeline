# Real-Time-Weather-Streaming-Pipeline
## Overview
This repository showcase a real-time data streaming pipeline that collects weather data from the OpenWeather, streams it through Apache  Kafka and stores it in Apache Cassandra for time-series analysis.

It demonstrates how modern data engineering systems handle real-time ingestion, streaming and storage of continously generated data.

<img width="1693" height="929" alt="Image May 23, 2026" src="https://github.com/user-attachments/assets/9d35905a-3c1e-47c1-9a71-35126d5683b9" />

## Architecture

    OpenWeather API
      ↓
    Kafka Producer (Python)
      ↓
    Kafka Topic: weather-data
      ↓
    Kafka Consumer
      ↓
    Apache Cassandra 

## Tech Stack
`- Python 3.x`

`- Kafka(Local/Confluent Cloud)`

`- Cassandra`

`- Requests (API calls)`

`- Kafka -Python`

`- Cassandra-driver`

## Project Structure

    weather-streaming-pipeline/
    │
    ├── producer/
    │   └── weather_producer.py
    │
    ├── consumer/
    │   └── weather_consumer.py
    │
    ├── config/
    │   └── config.py
    │
    ├── requirements.txt

# Setup Installation
## 1. Clone Repository
    git clone https://github.com/wachira-samuel/Real-Time-Weather-streaming-pipeline.git
    cd Real-Time-Weather-streaming-pipeline

## 2. Install Dependencies
    pip install -r requirements.txt

## 3. Start Kafka
If running locally:

    # Start Zookeeper
    zookeeper-server-start.sh config/zookeeper.properties

    # Start Kafka broker
    kafka-server-start.sh config/server.properties
Create topic:
```
kafka-topics.sh --create \
--topic weather-data \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```
## 4. Start Cassandra
``cassandra -f``
    
Verify:``cqlsh``

## Configuration
Create a .env or update config:
```
API_KEY = "YOUR_OPENWEATHER_API_KEY"
CITY = "Nairobi"
KAFKA_BROKER = "localhost:9092"
TOPIC = "weather-data"
```

# Running the Project
## 1. Start Producer 
```python producer/weather_producer.py```

## 2. Start Consumer 
``` python consumer/weather_consumer.py```

## Cassandra Schema

    CREATE KEYSPACE weather
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

    CREATE TABLE weather_data (
    city TEXT,
    timestamp BIGINT,
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    weather TEXT,
    PRIMARY KEY (city, timestamp)
    );
 ## Data Flow Explanation
 `1. Producer fetches real-time weather data from OpenWeather API`.
 
 `2. Data is serialized into JSON format`.
 
 `3. Kafka streams the data via weather-data topic`.
 
 `4. Consumer reads message in real-time.`
 
 `5. Data is stored in Cassandra for persistence and analysis.`

 ## Sample Output
 Producer
<img width="1308" height="393" alt="image" src="https://github.com/user-attachments/assets/c7d261f9-45e8-4d8c-8f63-9801af031a6a" />


Consumer
<img width="1601" height="313" alt="image" src="https://github.com/user-attachments/assets/d1790256-e491-4347-a628-800758bdf54a" />

 ## License
This project is for educational purposes.
    
