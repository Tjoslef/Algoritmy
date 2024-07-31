import math
from graphviz import Digraph
import numpy as np
import matplotlib.pyplot as plt
class Value:
    def __init__(self,data, _children=(), _op='', label=''):
        self.data = data
        self._prev = set(_children)
        self._op= _op
        self.label = label
        self.grad = 0.0
    def __repr__(self):
        return f"Value(data={self.data})"
    def __add__(self,other):
        out = Value(self.data + other.data,(self,other), '+' )
        return out
    def __mult__(self,other):
        out = Value(self.data * other.data,(self,other), '*')
        return out
#grafick0 vyzobrazeni
def trace(root):
    nodes, edges = set(),set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child,v))
                build(v)
    build(root)
    return nodes, edges
def draw_dot(root):
    dot= Digraph(format='svg',graph_attr={'rankdir': 'LR'})

    nodes,edges= trace(root)
    for n in nodes:
        uid = str(id(n))
        dot.node(name = uid, label = "{ %s | data %.4f | grad %.4f }" % (n.label, n.data, n.grad), shape='record')
        if n._op:
            dot.node(name = uid +n._op, label= n._op)
            dot.edges(uid + n._op,uid)
    for n1,n2 in edges:
        dot.edges(str(id(n1)), str(id(n2)) + n2._op)
    return dot
a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
e = a+b; e.label = 'e'
d = e + c; d.label = 'd'
f = Value(-2.0, label='f')
L = d + f; L.label = 'L'
draw_dot(L)



