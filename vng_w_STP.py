#!/usr/bin/python

"""
This imports config from a VirtualNetworkGraph.py .out file and creates
a network with the same node connectivity.
"""
import sys
import argparse

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.nodelib import LinuxBridge

def createNet(filename):
    linkList = []
    switchList = []
    hostList = []
 
    "Create an empty network and add nodes to it."
    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    try:
        f = open(filename)
    except IOError:
        print "Cannot open config file! Aborting..."
        sys.exit()

    for line in f:
        if (len(line.split()) > 3):
            continue 
        else:
            # Parse lines and create a list of link pairs
            node1, node2, weight = line.split()
            s1 = "s"+str(node1).strip()
            s2 = "s"+str(node2).strip()
            linkList.append((s1,s2))
            h1 = "h"+str(node1).strip()
            h2 = "h"+str(node2).strip()
            if h1 not in hostList:
              hostList.append(h1)
            if h2 not in hostList:
              hostList.append(h2)
            
    f.close()

    info( '*** Adding switches\n' )
    for (node1,node2) in linkList:
	if node1 not in switchList:
	    switchList.append(node1)
	    net.addSwitch(node1, cls=LinuxBridge, stp=True)
	    #print switchList
        if node2 not in switchList:
            switchList.append(node2)
	    net.addSwitch(node2, cls=LinuxBridge, stp=True)
	    #print switchList 

    info( '*** Adding hosts\n' )
    for host in hostList:
        net.addHost(host)

    nodes = [node for node in switchList]
    currHost = 0
    # Expects specific filenames. :\
    if (filename == "linear.out"):
        info( '*** Creating switch and host links for LINEAR network\n' )
        for (node1,node2) in linkList:
  	    net.addLink(node1,node2)
   	    net.addLink(hostList[currHost],node1)
	    currHost = currHost + 1 
        # Add last host to last node2 switch...
        net.addLink(hostList[currHost], linkList[currHost-1][1])
    elif ((filename == "full.out") or (filename == "random.out")):
        info( '*** Creating switch and host links for FULL network\n' )
        for (node1, node2) in linkList:
            net.addLink(node1,node2)
            # Stops duplicate additions where a switch has connected neighbors
            if node1 in nodes:
                net.addLink(hostList[currHost],node1)
                nodes.remove(node1) 
                currHost = currHost + 1
    elif (filename == "star.out"):
        info( '*** Creating switch and host links for STAR network\n' )
        for (node1, node2) in linkList:
            net.addLink(node1,node2)
            net.addLink(hostList[currHost], node2)
            currHost = currHost + 1 
        # Add last host to root switch, s0; still maintains star configuration
        net.addLink(hostList[currHost], linkList[0][0])


    info( '*** Starting network\n')
    net.start()

    ### Comment out next 2 lines if you don't want this...
    # Need STP or something better to handle multiple links
    if ((filename == "full.out") or (filename == "random.out")):
      info( '*** Wait for STP convergence...\n')
      net.waitConnected()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=sys.argv[0], usage="python %(prog)s <configfile>")
    parser.add_argument('filename')
    try:
        args = parser.parse_args()
    except IOError:
        parser.print_help()
        sys.exit(2)


    setLogLevel( 'info' )
    createNet(args.filename)
