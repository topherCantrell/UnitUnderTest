
# https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid
# https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf

import serial
import time
ser = serial.Serial('/dev/serial0',115200)

NULL_CHAR = chr(0)

KEY_MAP = {
    '0' : NULL_CHAR*2+chr(39)+NULL_CHAR*5,
    #
    ')' : chr(32)+NULL_CHAR+chr(39)+NULL_CHAR*5,
    '!' : chr(32)+NULL_CHAR+chr(30)+NULL_CHAR*5,
    '@' : chr(32)+NULL_CHAR+chr(31)+NULL_CHAR*5,
    '#' : chr(32)+NULL_CHAR+chr(32)+NULL_CHAR*5,
    '$' : chr(32)+NULL_CHAR+chr(33)+NULL_CHAR*5,
    '%' : chr(32)+NULL_CHAR+chr(34)+NULL_CHAR*5,
    '^' : chr(32)+NULL_CHAR+chr(35)+NULL_CHAR*5,
    '&' : chr(32)+NULL_CHAR+chr(36)+NULL_CHAR*5,
    '*' : chr(32)+NULL_CHAR+chr(37)+NULL_CHAR*5,
    '(' : chr(32)+NULL_CHAR+chr(38)+NULL_CHAR*5,
    #
    '\n' : NULL_CHAR*2+chr(40)+NULL_CHAR*5,
    ' ' : NULL_CHAR*2+chr(44)+NULL_CHAR*5,
    #
    '-' : NULL_CHAR*2+chr(45)+NULL_CHAR*5,
    '_' : chr(32)+NULL_CHAR+chr(45)+NULL_CHAR*5,
    #
    '.' : NULL_CHAR*2+chr(55)+NULL_CHAR*5,
    '>' : chr(32)+NULL_CHAR+chr(55)+NULL_CHAR*5,
    #
    '/' : NULL_CHAR*2+chr(56)+NULL_CHAR*5,
    '?' : chr(32)+NULL_CHAR+chr(56)+NULL_CHAR*5,
    #
    ';' : NULL_CHAR*2+chr(51)+NULL_CHAR*5,
    ':' : chr(32)+NULL_CHAR+chr(51)+NULL_CHAR*5,
    #
    # Temporary hack for down arrow
    #
    '|' : NULL_CHAR*2+chr(81)+NULL_CHAR*5,
}

for i in range(26):
    letter = chr(ord('a')+i)
    KEY_MAP[letter] = NULL_CHAR*2+chr(i+4)+NULL_CHAR*5
    KEY_MAP[letter.upper()] = chr(32)+NULL_CHAR+chr(i+4)+NULL_CHAR*5
    
for i in range(9):
    letter = chr(ord('1')+i)
    KEY_MAP[letter] = NULL_CHAR*2+chr(i+30)+NULL_CHAR*5
    
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
        
def type_key(k):
    if k in KEY_MAP:
        write_report(KEY_MAP[k])
        write_report(NULL_CHAR*8)
        
while True:
    s = ser.read(1).decode()
    type_key(s)
    time.sleep(.25)
    