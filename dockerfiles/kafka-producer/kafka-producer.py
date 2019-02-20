from kafka import KafkaProducer
import time
from time import sleep
from analog_sensor import sensor_reading
from anomaly_detection import check_anomaly
import json

def initialize():
    producer = KafkaProducer(bootstrap_servers=['128.195.53.171:9092'],value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    return producer

if __name__ == '__main__':
    producer = initialize()
    while True:
        analog_sensor_value = sensor_reading()
        anomaly_flag = check_anomaly(analog_sensor_value)
        print(anomaly_flag)
        producer.send('test',value=analog_sensor_value)
        time.sleep(10)   
