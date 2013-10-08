#!/usr/bin/env python

import bluetooth, os, struct, sys
from PyOBEX import client, headers

if __name__ == "__main__":

    if len(sys.argv) != 4:
    
        sys.stderr.write("Usage: %s <device address> <port> <file name>\n" % sys.argv[0])
        sys.exit(1)
    
    device_address = sys.argv[1]
    port = int(sys.argv[2])
    file_name = sys.argv[3]
    
    c = client.Client(device_address, port)
    c.connect(header_list=(headers.Target("OBEXObjectPush"),))
    c.put(file_name, open(file_name).read())
    c.disconnect()

    sys.exit()
