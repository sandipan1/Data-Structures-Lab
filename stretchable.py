# Make stretchable array
'''from ctypes import *
class DynamicTable:
	def __init__(self):
		self.curcap=0
		self.maxcap=2
		self.arr=(c_type * 2)(0)
	def add(self,x):
		if self.curcap== self.maxcap-1:
			self.maxcap+=1
			ar=c_type * self.maxcap
			for i in range(self.curcap):
				ar[i]=self.arr[i]
			self.curcap+=1
			ar[self.curcap]=x
			self.arr=(c_type * self.maxcap)()
			for i in range(self.maxcap):
				self.arr[i]=ar[i]

		elif (self.curcap < self.maxcap):
			self.curcap+=1
			self.arr[self.curcap]=x

	def delete(self):
		ar=(c_type *(self.maxcap-1))()
		for i in range(self.maxcap-1):
			self.arr'''


from ctypes import *
import random 
from time import *

class stretchable_array:
  def __init__(self, L):
    self.L = (c_int*1)()
    self.L[0] = L
    self.count = 1
  
  def __repr__(self):
    rep = ""
    for i in range(self.count):
      rep += str(self.L[i]) + " "
    return rep
  
  def insert(self,x):
    if self.count >= len(self.L):
      M = self.L
      lenth = len(M) *2
      self.L = (c_int*lenth)()
      for i in range(len(M)):
        self.L[i] = M[i]
      self.L[self.count] = x      
    else:
      self.L[self.count] = x
    self.count = self.count+1
  def remove(self):
    if self.count > len(self.L)/4 :
      M = self.L
      self.L = (c_int*len(self.L))()
      self.L = M[0:-1]
      self.count -= 1
    else:
      M = self.L
      self.L = (c_int*(len(self.L)/2))
      self.L = M[0:-1]
      self.count -= 1

A = stretchable_array(4)
print A
time1 = time()
for i in range(10):
  A.insert(random.choice(range(10)))
time2 = time()


B = [4]
time3 = time()
for i in range(10):
  B += [random.choice(range(10))]
time4 = time()
#print B

print ("{0} {1} ".format(time2-time1, time4 - time3))


