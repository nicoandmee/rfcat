#!/usr/bin/python

from __future__ import print_function

import sys
import serial

port = sys.argv.pop() if len(sys.argv) > 1 else "ACM0"
dport = f"/dev/tty{port}"

print(f"Opening serial port {dport} for listening...")
s=serial.Serial(dport, 115200)

counter = 0
while True:
    print("%d: %s" % (counter, repr(s.read(12))))
    counter += 1
    #sys.stdout.write(s.read(1))
    #sys.stdout.flush()
