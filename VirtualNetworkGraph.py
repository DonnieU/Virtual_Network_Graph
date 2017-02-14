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
    topology = str(rhs).strip()  # removes leading and ending whitespace
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
