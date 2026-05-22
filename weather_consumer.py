from kafka import KafkaConsumer
from cassandra.cluster import Cluster
import json

# Kafka consumer
consumer = KafkaConsumer(
    'weather-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Cassandra connection
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

session.execute("""
CREATE KEYSPACE IF NOT EXISTS weather
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")

session.set_keyspace('weather')

session.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    city TEXT,
    timestamp BIGINT,
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    weather TEXT,
    PRIMARY KEY (city, timestamp)
)
""")

print("Consumer running...")

for message in consumer:
    data = message.value

    session.execute("""
        INSERT INTO weather_data (city, timestamp, temperature, humidity, pressure, weather)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data["city"],
        data["timestamp"],
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["weather"]
    ))

    print("Stored in Cassandra:", data)