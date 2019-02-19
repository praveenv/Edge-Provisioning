#!/usr/bin/env python

def check_anomaly(sensor_value):
    if sensor_value < 100:
        return True
    elif sensor_value > 100:
        return False
