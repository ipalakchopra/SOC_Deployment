from kafka import KafkaConsumer
import json

# Input for consumer group
#group = input("Enter consumer group: ")

# Kafka consumer setup
consumer = KafkaConsumer(
    'sys_topic',
    group_id="sys_group",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    #value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consumer logic
for message in consumer:
    print(f"{message}")