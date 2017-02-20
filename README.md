# Virtual Network Graph and mininet script

Built with: Python 2.7.11 on Linux version 4.3.0-xxxxx-amd64

To run:
```
python VirtualNetworkGraph.py <configfile>
```

where *configfile* contains the following format:

nodes:          4<br>
topology:       LINEAR<br>
alpha:          0.32<br>
node-min:       20<br>
node-max:       40<br>
link-min:       10<br>
link-max:       30<br>

##### Notes:

*topology* is case insensitive and supports Linear, Full, Star, & Random;<br>
*alpha* range: 0.0 <= alpha <= 1.0;

See included *.txt files for examples;

Program outputs a *topology.out* file containing this layout:<br>
Source-Node-ID&nbsp;&nbsp;&nbsp;&nbsp;Destination-ID&nbsp;&nbsp;&nbsp;&nbsp;Link0-weight<br>
Source-Node-ID&nbsp;&nbsp;&nbsp;&nbsp;Destination-Node-ID&nbsp;&nbsp;&nbsp;&nbsp;Link1-weight<br>
...<br>
Node0-weight&nbsp;&nbsp;&nbsp;&nbsp;Node1-weight&nbsp;&nbsp;&nbsp;&nbsp;...&nbsp;&nbsp;&nbsp;&nbsp;NodeN-weight<br>

See *.out files for examples

### vng.py = mininet script using *.out* files from VirtualNetworkGraph.py
This script will build a network in mininet with the same connectivity found in the *.out* file<br>

To use:
* Launch mininet
* From CLI, run:
```
sudo python vng.py <filename.out>
```
where *filename.out* is an output file from VirtualNetworkGraph.py<br>
