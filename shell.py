#!/usr/bin/env python3

import os
import getpass
import socket
import helpcmd

username = getpass.getuser()
hostname = socket.gethostname().split('.')[0]

def shell():
    while True:
        cdir = os.getcwd()
        command = input(f"{username}@{hostname}:{cdir}-> ").strip()
        parts = command.split()
        if len(parts) == 0:
            continue
        if parts[0] == 'cd':
            try:
                if len(parts) > 1:
                    os.chdir(parts[1])
                else:
                    os.chdir(os.path.expanduser("~"))
            except FileNotFoundError as e:
                print(f"cd: {e}")
        elif parts[0] == 'exit':
            break
        elif parts[0] == 'helpcmd':
            helpcmd.init()
        else:
            os.system(command)

if __name__ == "__main__":
    shell()
