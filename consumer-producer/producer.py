# producer.py

import time
from kafka import SimpleProducer, KafkaClient
from kafka import KafkaProducer
#  connect to Kafka
# kafka = Kafka.SimpleClient('localhost:9092')
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9093')
# Assign a topic
topic = 'stats'

for _ in range(100):
    producer.send('foobar', b'some_message_bytes')
