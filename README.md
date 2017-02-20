# Virtual_Network_Graph

Built with: Python 2.7.11 on Linux version 4.3.0-kalil-amd64

To run:

python VirtualNetworkGraph.py <configfile>

where <configfile> contains the following format:

nodes:          4
topology:       LINEAR
alpha:          0.32
node-min:       20
node-max:       40
link-min:       10
link-max:       30

*Note:
topology is case insensitive and supports Linear, Full, Star, & Random;
alpha range: 0.0 <= alpha <= 1.0;
See included *.txt files for examples;

Program outputs a <topology>.out file containing this layout:

Source-Node-ID    Destination-Node-ID    Link0-weight
Source-Node-ID    Destination-Node-ID    Link1-weight
...
Node0-weight    Node1-weight    ...    NodeN-weight

*See including *.out files for examples
