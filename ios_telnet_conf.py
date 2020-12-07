#!/usr/bin/python3

from telnetlib import Telnet
from getpass import getpass


PORT = 23
TIMEOUT = 10
t_pass = getpass("Provide telnet password to devices: ")
e_pass = getpass("Provide enable password to devices: ")

with open('configuration', 'rb') as f:
    configuration = f.read()

with open('hosts', 'r') as f:
    hosts = f.read().splitlines()

for host in hosts:
    try:
        conn = Telnet(host, PORT, TIMEOUT)
    except OSError as  err:
        print(f"Could not connect to host {host}: {err}")
        continue

    conn.read_until(b"Password: ")
    conn.write(t_pass.encode('ascii') + b"\n")
    conn.write(b"enable\n")
    conn.write(e_pass.encode('ascii') + b"\n")
    conn.write(b"configure terminal\n")
    conn.write(configuration + b"\n")
    conn.write(b"end\nexit\n")

    print(conn.read_all().decode())
    conn.close()
