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

def createNet(filename):
    linkList = []
    switchList = []
    
    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    #info( '*** Adding hosts\n' )
    #h1 = net.addHost( 'h1', ip='10.16.0.1/24' )
    #h2 = net.addHost( 'h2', ip='10.16.0.2/24' )

    info( '*** Adding switches\n' )
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
            node1 = "s"+str(node1).strip()
            node2 = "s"+str(node2).strip()
            linkList.append((node1,node2))
            
    f.close()

    # Add switches 
    for (node1,node2) in linkList:
	if node1 not in switchList:
	    switchList.append(node1)
	    net.addSwitch(node1)
	    #print switchList
        if node2 not in switchList:
            switchList.append(node2) 
	    net.addSwitch(node2)
	    #print switchList 
	    #net.addLink(node1, node2)

    info( '*** Creating links\n' )
    for (node1,node2) in linkList:
        net.addLink(node1,node2)
     
    info( '*** Starting network\n')
    net.start()

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
