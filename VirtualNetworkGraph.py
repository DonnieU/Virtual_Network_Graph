import sys
import argparse
import random

class Vertex:
  def __init__(self, node):
    self.id = node
    self.adjacent = {}

  def __str__(self):
    return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

  def add_neighbor(self, neighbor, weight=0):
    self.adjacent[neighbor] = weight

  def get_connections(self):
    return self.adjacent.keys()

  def get_id(self):
    return self.id

  def get_weight(self, neighbor):
    return self.adjacent[neighbor]

class Graph:
  def __init__(self):
    self.vert_dict = {}
    self.num_vertices = 0
    self.num_nodes = 0
    self.topology = ""
    self.alpha = 0
    self.node_min = 0
    self.node_max = 0
    self.link_min = 0
    self.link_max = 0

  def __iter__(self):
    return iter(self.vert_dict.values())

  def add_vertex(self, node):
    self.num_vertices = self.num_vertices + 1
    new_vertex = Vertex(node)
    self.vert_dict[node] = new_vertex
    return new_vertex

  def get_vertex(self, n):
    if n in self.vert_dict:
      return self.vert_dict[n]
    else:
      return None

  def add_edge(self, src, dest, weight = 0):
    if src not in self.vert_dict:
      self.add_vertex(src)
    if dest not in self.vert_dict:
      self.add_vertex(dest)

    self.vert_dict[src].add_neighbor(self.vert_dict[dest], weight)
    self.vert_dict[dest].add_neighbor(self.vert_dict[src], weight)

  def get_vertices(self):
    return self.vert_dict.keys()

  def set_num_nodes(self, n):
    self.num_nodes = n

  def get_num_nodes(self):
    return self.num_nodes

  def set_topology(self, topo):
    self.topology = topo

  def get_topology(self):
    return self.topology

  def set_alpha(self, a):
    self.alpha = a

  def get_alpha(self):
    return self.alpha

  def set_node_min(self, n):
    self.node_min = n

  def get_node_min(self):
    return self.node_min
 
  def set_node_max(self, n):
    self.node_max = n

  def get_node_max(self):
    return self.node_max

  def set_link_min(self, n):
    self.link_min = n

  def get_link_min(self):
    return self.link_min

  def set_link_max(self, n):
    self.link_max = n

  def get_link_max(self):
    return self.link_max

def print_graph(g):
  for v in g:
    for w in v.get_connections():
      vid = v.get_id()
      wid = w.get_id()
      print '(%s, %s, %3d)' % ( vid, wid, v.get_weight(w))

  for v in g:
    print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])


if __name__ == '__main__':
  """
  g = Graph()
  
  g.add_vertex('a')
  g.add_vertex('b')
  g.add_vertex('c')
  g.add_vertex('d')
  g.add_vertex('e')
  g.add_vertex('f')

  g.add_edge('a', 'b', 7)
  g.add_edge('a', 'c', 9)
  g.add_edge('a', 'f', 14)
  g.add_edge('b', 'c', 10)
  g.add_edge('b', 'd', 15)
  g.add_edge('c', 'd', 11)
  g.add_edge('c', 'f', 2)
  g.add_edge('d', 'e', 6)
  g.add_edge('e', 'f', 9)

  for v in g:
    for w in v.get_connections():
      vid = v.get_id()
      wid = w.get_id()
      print '(%s, %s, %3d)' % ( vid, wid, v.get_weight(w))

  for v in g:
    print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])
  """

  #f = open('four_node_linear_config.txt')
  #print f.read()
  topology = ""
  alpha = 0
  link_max = 0

  # Parse and check command line arguments...
  parser = argparse.ArgumentParser(prog=sys.argv[0], usage="python %(prog)s <configfile>")
  parser.add_argument('filename')
  try:
    args = parser.parse_args()
  except IOError:
    parser.print_help()
    sys.exit(2)
    
  try:
    f = open(args.filename)
  except IOError:
    print "Cannot open config file! Aborting..."
    sys.exit()

  g = Graph()

  for line in f:
    lhs, rhs = line.split(":")
    #print lhs, rhs
    if (lhs == "nodes"):
      g.set_num_nodes(int(rhs))
    elif (lhs == "topology"):
      g.set_topology(str(rhs).strip().lower())  # removes leading and ending whitespace; makes lowercase
    elif ((topology == "random") and (lhs == "alpha")):
      g.set_alpha(int(rhs))
    elif (lhs == "node-min"):
      g.set_node_min(int(rhs))
    elif (lhs == "node-max"):
      g.set_node_max(int(rhs))
    elif (lhs == "link-min"):
      g.set_link_min(int(rhs))
    elif (lhs == "link-max"):
      g.set_link_max(int(rhs))
    else:
      continue

  f.close()

  print "nodes: " + str(g.get_num_nodes()) 
  print "topology: " + g.get_topology() + " " + str(len(g.get_topology()))
  print "alpha: " + str(g.get_alpha())
  print "link_max: " + str(g.get_link_max())
  for i in range(g.get_num_nodes()):
    weight = int(random.uniform(g.get_link_min(), g.get_link_max()))
    print "random.uniform for link weight: " + str(weight) 
  #print g.__dict__

  if (g.get_topology() == "linear"):
    for i in range(g.get_num_nodes()-1):
      link_weight = int(random.uniform(g.get_link_min(), g.get_link_max()))
      g.add_edge(i,i+1,link_weight)
      
  #print_graph(g) 
  print g.get_vertices()
