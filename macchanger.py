#!/usr/bin/python

import subprocess
from termcolor import colored

def change_mac_address(interface,mac):
    
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

def main():
    interface = str(input("[*] Enter Interface To Change Mac Address On: "))
    new_mac_address = input("[*] Enter Mac Address To Change To: ")

    before_change = subprocess.check_output(["ifconfig",interface])
    change_mac_address(interface,new_mac_address)
    after_change = subprocess.check_output(["ifconfig",interface])

    if before_change == after_change:
        print(colored("[!!] Failed To Change Mac Address To: " + new_mac_address, 'red'))
    else:
        print(colored("[+] MAC Address Changed To: " + new_mac_address + " On Interface: " + interface,'green'))

main()