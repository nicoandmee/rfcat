#!/usr/bin/env python3
from __future__ import print_function
import sys

sn_header = """// Serial number
               10,                      // bLength
               USB_DESC_STRING,         // bDescriptorType
"""

try:
    with open('.serial', 'r') as f:
        ser = int(f.read(), 16) #+ 1
except IOError:
    ser = 0

print("[--- new serial number: %.4x ---]" % ser, file=sys.stderr)

with open('.serial', 'w') as f:
    f.write("%.4x" % ser)
sertxt = "%.4x" % ser

for c in sertxt:
    n = ord(c)
    sys.stdout.write(f"{n},0,")

