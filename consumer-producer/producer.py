#producer.py

import time
from kafka import SimpleProducer, KafkaClient
from kafka import KafkaProducer
# #  connect to Kafka
# # kafka = Kafka.SimpleClient('localhost:9092')
# producer = KafkaProducer(bootstrap_servers='kafka:9092')
# # Assign a topic
# topic = 'stats'

# for _ in range(50):
#     producer.send(topic, b'chaito')

#     #post 

producer = KafkaProducer(bootstrap_servers='kafka:9092')
for _ in range(100):
    time.sleep(2)
    producer.send('stats', b'some_message_bytes')
