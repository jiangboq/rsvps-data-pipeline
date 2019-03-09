import websocket
from kafka import KafkaProducer

def on_message(ws, message):
    producer.send('meetupTopic', message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    pass

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://stream.meetup.com/2/rsvps",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()