from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer('meetupTopic')
    
    for message in consumer:
        print (message)