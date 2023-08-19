#!/usr/bin/env python3

from __future__ import print_function

import sys
from rflib.intelhex import IntelHex

WRITEBACK = True
if len(sys.argv) > 1:
    WRITEBACK = False
    ser = int(sys.argv[1])
else:
    try:
        serbytes = open(".serial", 'rb').read()
        ser = int(serbytes, 16) + 1
    except (IOError, ValueError):
        ser = 0

print(("[--- new serial number: %.4x ---]" % ser), file=sys.stderr)

if WRITEBACK:
    open(".serial", 'wb').write(b"%.13x" % ser)

sertmp = "%.13x" % ser
sertxt = ''.join("%s\x00" % c for c in sertmp)
ihc=IntelHex('CCBootloader/CCBootloader-rfcat-chronosdongle.hex')
ihd=IntelHex('CCBootloader/CCBootloader-rfcat-donsdongle.hex')
ihy=IntelHex('CCBootloader/CCBootloader-rfcat-ys1.hex')
ihc.puts(0x13e0, "@las\x1c\x03" + sertxt)
ihd.puts(0x13e0, "@las\x1c\x03" + sertxt)
ihy.puts(0x13e0, "@las\x1c\x03" + sertxt)
ihc.write_hex_file('CCBootloader/CCBootloader-rfcat-chronosdongle-serial.hex')
ihd.write_hex_file('CCBootloader/CCBootloader-rfcat-donsdongle-serial.hex')
ihy.write_hex_file('CCBootloader/CCBootloader-rfcat-ys1-serial.hex')

