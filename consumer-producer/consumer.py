from flask import Flask, Response
from kafka import KafkaConsumer
# #connect to Kafka server and pass the topic we want to consume
# consumer = KafkaConsumer('stats', group_id='view',bootstrap_servers=['kafka:9092'])
# #Continuously listen to the connection and print messages as recieved
# app = Flask(__name__)

# @app.route('/')
# def index():
#     # return a multipart response
#     return Response(kafkastream())
    
# def kafkastream():
#     for msg in consumer:
#         print(msg)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
consumer = KafkaConsumer('stats', group_id='view',bootstrap_servers=['kafka:9092'])
for msg in consumer:
    print (msg)