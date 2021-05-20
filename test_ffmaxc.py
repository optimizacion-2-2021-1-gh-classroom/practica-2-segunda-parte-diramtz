from pytest import approx
from ffmaxc import *
import networkx as nx

#Resolvemos usando networkx
G = nx.DiGraph()

G.add_edge('o', 'a', capacity=5)
G.add_edge('o', 'b', capacity=7)
G.add_edge('o', 'c', capacity=4)

G.add_edge('a', 'b', capacity=1)
G.add_edge('a', 'd', capacity=3)

G.add_edge('b', 'c', capacity=2)
G.add_edge('b', 'd', capacity=4)
G.add_edge('b', 'e', capacity=5)

G.add_edge('c', 'e', capacity=4)

G.add_edge('d', 't', capacity=9)

G.add_edge('e', 'd', capacity=1)
G.add_edge('e', 't', capacity=9)

flow_value, flow_dict = nx.maximum_flow(G, 'o', 't')


#Resolvemos usando nuestro paquete MaxFlow

red = create_flow_network()

red.create_vertex('o', True, False) 
red.create_vertex('t', False, True) 
red.create_vertex('a', False, False)
red.create_vertex('b', False, False)
red.create_vertex('c', False, False)
red.create_vertex('d', False, False)
red.create_vertex('e', False, False)

red.create_edge('o', 'a', 5)
red.create_edge('o', 'b', 7)
red.create_edge('o', 'c', 4)

red.create_edge('a', 'b', 1)
red.create_edge('a', 'd', 3)

red.create_edge('b', 'c', 2)
red.create_edge('b', 'd', 4)
red.create_edge('b', 'e', 5)

red.create_edge('c', 'e', 4)

red.create_edge('d', 't', 9)

red.create_edge('e', 'd', 1)
red.create_edge('e', 't', 9)

red.MaxFlow()

def test_vals_1():
    assert(red.MaxFlow() == flow_value)
