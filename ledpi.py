import os
import RPi.GPIO as GPIO


class Ledpi:
    def __init__(self, channels):
        self.channels = channels
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup(self.channels)
        for channel in self.channels:
            GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
   
    def on(self, channel):
        try:
            if channel not in self.channels:
                raise Exception("Invalid channel input {}".format(channel))
            if GPIO.input(channel) == GPIO.LOW:
                GPIO.output(channel, GPIO.HIGH)
                return "SUCCESS", "channel {} is set to HIGH".format(channel)
            return "NOCHANGE", "channel {} was already set to HIGH".format(channel)
        except Exception as e:
            return "FAILURE", e.message 

    def off(self, channel):
        try:
            if channel not in self.channels:
                raise Exception("Invalid channel input {}".format(channel))
            if GPIO.input(channel) == GPIO.HIGH:
                GPIO.output(channel, GPIO.LOW)
                return "SUCCESS", "channel {} is set to LOW".format(channel)
            return "NOCHANGE", "channel {} was already set to LOW".format(channel)
        except Exception as e:
            return "FAILURE", e.message 

    def state(self, channel):
        print(channel, self.channels)
        try:
            if channel not in self.channels:
                raise Exception("Invalid channel input {}".format(channel))
            state = "HIGH" if GPIO.input(channel) == 1 else "LOW"
            return "SUCCESS", "State of {} is {}".format(channel, state)
        except Exception as e:
            return "FAILURE", e.message 


    
