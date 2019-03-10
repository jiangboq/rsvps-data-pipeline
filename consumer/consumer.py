'''from pyspark import SparkContext'''
'''from pyspark.streaming import StreamingContext'''
from kafka import KafkaConsumer

def createContext():
    pass

if __name__ == "__main__":
    consumer = KafkaConsumer('meetupTopic')
    
    for message in consumer:
        print (message)