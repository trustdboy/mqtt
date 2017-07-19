import paho.mqtt.client as mqtt
from gpiozero import LED
from signal import pause
from time import sleep

def on_message(client, userdata, message):
    print message.payload
    dash()
    
def on_connect(client, userdata, flags, code):
    print"connected: " + str(code)
    client.subscribe("test/all")


led = LED(17)

def dash():
        led.on()        
       sleep(0.5)
        led.off()
        sleep(1)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("moorhouseassociates.com", 1883, 60)

client.loop_forever()
pause()
