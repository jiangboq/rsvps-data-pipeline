from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from bson import json_util
import json

def createContext():
    pass

if __name__ == "__main__":
    consumer = KafkaConsumer(
        'meetupTopic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    
    client = MongoClient('localhost:27017')
    db = client['meetup_db']
    collection = db['rsvps'] 
    
    for message in consumer:
        message = message.value
        collection.insert_one(json.loads(message))
        print ('{} added to {}'.format(message, collection))