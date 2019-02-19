#!/usr/bin/env python

import spidev

def spi_init():
    adc_channel = 2
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 20000
    return adc_channel, spi

def readadc(spi,adc_channel):
    if adc_channel > 7 or adc_channel < 0:
        return -1
    adc_reading = spi.xfer2([1, 8 + adc_channel << 4, 0])
    adc_output = (( adc_reading[1] & 3 ) << 8) + adc_reading[2]
    print(adc_output)
    return adc_output

def sensor_reading():
    adc_channel, spi = spi_init()
    while True:
        value = readadc(spi,adc_channel)
        return value
