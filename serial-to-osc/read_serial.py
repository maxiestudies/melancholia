
from pythonosc import udp_client
import serial
import sys
import ipdb

ser = serial.Serial('/dev/ttyUSB0', 115200)
client = udp_client.SimpleUDPClient('127.0.0.1', 7899)

while True:
    try:
        msg = ser.read(6)
        msg_list = list(msg)
        sensor_1_list = msg[2:4]
        sensor_1 = int.from_bytes(sensor_1_list, byteorder="little")
        sensor_2_list = msg[4:]
        sensor_2 = int.from_bytes(sensor_2_list, byteorder="little")

        # for debugging
        # print(f"button 1: {msg_list[0]}, button 2: {msg_list[1]}, sensor 1: {sensor_1}, sensor 2: {sensor_2}")

        # send osc
        client.send_message("/button/one", msg_list[0])
        client.send_message("/button/two", msg_list[1])
        client.send_message("/sensor/one", sensor_1)
        client.send_message("/sensor/two", sensor_2)
    except KeyboardInterrupt:
        print("Interrupted",end="")
        sys.exit(0)
