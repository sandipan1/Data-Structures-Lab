# Make stretchable array
from ctypes import *
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
			self.arr



