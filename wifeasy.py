#!/usr/bin/env python2.7
import sys
import subprocess
import re

CMD_INTERFACES      = "iw dev | grep Interface"
CMD_START_INTERFACE = "sudo ip link set {0} up"
CMD_CONNECT_WEP     = "sudo iw dev {0} connect {1} key 0:{2}"
CMD_SCAN_NETWORKS   = "sudo iw dev {0} scan | grep SSID:"
RE_INTERFACES       = "Interface\s+(\w+)"
RE_SSID             = "SSID:\s+(\w+)"

def getInterface(index=None):
    if index==None:
        index = 0
    interfaces = getIntefaces()
    if len(interfaces)>index:
        return interfaces[index]

def getIntefaces():
    interfaces = subprocess.check_output([CMD_INTERFACES],shell=True)
    interfaces = re.findall(RE_INTERFACES,interfaces)
    return interfaces

def getNetworks(interface=None):
    if interface == None:
        interface=getInterface()
    cmd = getScanCmd(interface)
    networks = subprocess.check_output([cmd],shell=True)
    networks = re.findall(RE_SSID,networks)
    return networks

def connect(network,password,interface=None,networkType=None):
    if networkType == None:
        networkType = "wep"
    if interface == None:
        interface=getInterface()
    cmd = getConnectCmd(network,password,interface)

def getStartInterfaceCmd(interface):
    return CMD_START_INTERFACE.format(interface)

def getConnectCmd(network,key,interface):
    return CMD_CONNECT_WEP.format(interface,network,key)

def getScanCmd(interface):
    return CMD_SCAN_NETWORKS.format(interface)

def main():
    if len(sys.argv) == 1:
        print "interfaces",getIntefaces()
        print "Networks:",getNetworks()
    if len(sys.argv) >= 2:
        network = sys.argv[1]
    if len(sys.argv) >= 3:
        password = sys.argv[2]
    #print connect(network,password)
    
if __name__ == '__main__':
    main()