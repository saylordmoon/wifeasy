#!/usr/bin/env python2.7
import sys
import subprocess
import re

CMD_GET_INTERFACE   = "iw dev | grep Interface"
CMD_START_INTERFACE = "ip link set wls32 up"
CMD_CONNECT_WEP     = "iw dev {0} connect {1} key 0:{2}"
CMD_SCAN_NETWORKS   = "sudo iw dev wls32 scan | grep SSID:"
RE_INTERFACES       = "Interface\s+(\w+)"

def getInterface(index=None):
    if index==None:
        index = 0
    interfaces = getIntefaces()
    if len(interfaces)>index:
        return interfaces[index]

def getIntefaces():
    interfaces = subprocess.check_output([CMD_GET_INTERFACE],shell=True)
    interfaces = re.findall(RE_INTERFACES,interfaces)
    return interfaces

def connect(network,password,interface=None,networkType=None):
	if networkType == None:
		networkType = "wep"
    if interface == None:
        interface=getInterface()
	return getConnectCommand(interface,network,password)

def getConnectCommand(interface,network,key):
    return CMD_CONNECT_WEP.format(interface,network,key)

    
def main():

    # if len(sys.argv) >= 2:
    #     network = sys.argv[1]
    # if len(sys.argv) >= 3:
    #     password = sys.argv[2]
    print connect(network,password)

if __name__ == '__main__':
    main()
