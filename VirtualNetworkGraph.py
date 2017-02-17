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
      self.add_vertyex(dest)

    self.vert_dict[src].add_neighbor(self.vert_dict[dest], weight)
    self.vert_dict[dest].add_neighbor(self.vert_dict[src], weight)

  def get_vertices(self):
    return self.vert_dict.keys()
 
if __name__ == '__main__':
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
f = open('four_node_linear_config.txt')
#print f.read()
#config_list = []
topology = ""
alpha = 0
link_max = 0


for line in f:
  lhs, rhs = line.split(":")
  #print lhs, rhs
  if (lhs == "nodes"):
    nodes = int(rhs)
  elif (lhs == "topology"):
    topology = str(rhs).strip().lower()  # removes leading and ending whitespace; makes lowercase
  elif ((topology == "random") and (lhs == "alpha")):
    alpha = int(rhs)
  elif (lhs == "node-min"):
    node_min = int(rhs)
  elif (lhs == "node-max"):
    node_max = int(rhs)
  elif (lhs == "link-min"):
    link_min = int(rhs)
  elif (lhs == "link-max"):
    link_max = int(rhs)
  else:
    continue

f.close()

print "nodes: " + str(nodes) 
print "topology: " + topology + " " + str(len(topology))
print "alpha: " + str(alpha)
print "link_max: " + str(link_max)
for i in range(nodes):
  weight = int(random.uniform(link_min, link_max))
  print "random.uniform for link weight: " + str(weight) 
"""
