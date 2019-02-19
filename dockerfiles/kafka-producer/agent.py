#!/usr/bin/env python

from analog_sensor import analog_sensor
from anomaly_detection import check_anomaly
import time

if __name__ == '__main__':
    while True:
        analog_sensor_value = analog_sensor()
        anomaly_flag = check_anomaly(analog_sensor_value)
        time.sleep(1)
