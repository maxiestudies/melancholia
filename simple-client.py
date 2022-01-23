#!/usr/bin/env python

from pythonosc import udp_client
import time
import math
import sys

client = udp_client.SimpleUDPClient('127.0.0.1', 8765)

client.send_message('/send', sys.argv[1])
