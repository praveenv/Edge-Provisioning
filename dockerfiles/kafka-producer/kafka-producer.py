from kafka import KafkaProducer
from time import sleep
from analog_sensor import analog_sensor
from anomaly_detection import check_anomaly


def initialize():
    producer = KafkaProducer(bootstrap_servers=['128.195.53.171:9092'])

 if __name__ == '__main__':
    initialize()
    while True:
        analog_sensor_value = analog_sensor()
        print(analog_sensor_value)
        anomaly_flag = check_anomaly(analog_sensor_value)
        print(anomaly_flag)
        producer.send('test',anomaly_flag)
        time.sleep(10)   
