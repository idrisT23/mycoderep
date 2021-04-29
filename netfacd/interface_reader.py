#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def get_ip(data):
    try:
        return (data[netifaces.AF_INET])[0]['addr'] # Prints the IP address
    except:          # This is a new line
        return ('Could not get the IP address') # Print an error message
    

for i in netifaces.interfaces():
    ip_add = get_ip(netifaces.ifaddresses(i))
    print(f"Ip address is {ip_add}") # Prints the IP address
