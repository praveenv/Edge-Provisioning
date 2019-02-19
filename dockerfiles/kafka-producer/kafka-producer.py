from kafka import KafkaProducer
import time
from time import sleep
from analog_sensor import sensor_reading
from anomaly_detection import check_anomaly



def initialize():
    producer = KafkaProducer(bootstrap_servers=['128.195.53.171:9092'])
    return producer

if __name__ == '__main__':
    producer = initialize()
    while True:
        analog_sensor_value = sensor_reading()
        anomaly_flag = check_anomaly(analog_sensor_value)
        print(anomaly_flag)
        producer.send('test','True')
        time.sleep(10)   
