#!/usr/bin/python3
import random
import operator
class Graph:
  class vertex:
    def __init__(self,i):
      self.rank=None
      self.p=None
      self.number=i+1
  class Edge:
    def __init__(self,u,v):
      self.weight=int(random.uniform(1,20))
      self.start=u
      self.end=v
      u.p=v
  def __init__(self,n):
    self.V=[]
    for i in range(n):
      self.V.append(self.vertex(i))
    self.E=[]
    for i in range(len(self.V)):
      for j in range(i+1,len(self.V)):
        self.E.append(self.Edge(self.V[i],self.V[j]))
    for i in self.E:
      print(i.weight)
def MAKESET(i):
  i.p=i
  i.rank=0
def UNION(x,y):
  LINK(FINDSET(x),FINDSET(y))
def LINK(x,y):
  if x.rank>y.rank:
    y.p=x
  else:
    x.p=y
    if x.rank==y.rank:
      y.rank=y.rank+1
def FINDSET(x):
  if x!=x.p:
    x.p=FINDSET(x.p)
  return x.p
def MST(a):
   final=[]
   for v in a.V:
     MAKESET(v)
   a.E=sorted(a.E,key=operator.attrgetter('weight'))
   print("sorted")
   for i in a.E:
     print(i.weight)
   for i in a.E:
     #print(FINDSET(i.start).number!=FINDSET(i.end).number)
     if FINDSET(i.start)!=FINDSET(i.end):
       final.append(i)
       UNION(i.start,i.end)
   print("length",len(final))
   for i in final:
     print(i.weight,end=" ")
   for i in final:
     print("(",i.start.number,",",i.end.number,")",end=" ")
a=Graph(4)
MST(a)


