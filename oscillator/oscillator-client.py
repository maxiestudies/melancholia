#!/usr/bin/env python

from pythonosc import udp_client
import time
import math

client = udp_client.SimpleUDPClient('127.0.0.1', 8123)

while True:
    for i in range(0,20):
        output = math.cos((i/10) * math.pi)
        client.send_message('/test/one', output)
        time.sleep(1)
