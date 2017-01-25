#!/usr/bin/python3

# Operator Overloading
class Matrix:
	def __init__(self,a ):
		self.a=a
		self.r=len(self.a)
		self.c=len(self.a[0])
		
	def __add__(self,x):
		f=Matrix([[0 for i in range(self.c)] for j in range(self.r)])
		
		
		if self.r==x.r and self.c==x.c:
			for i in range(self.r):
				for j in range(self.c):
					f.a[i][j]=self.a[i][j]+x.a[i][j]
			return f
		
		else:
			print("error")
		
		
	def __mul__(self,x):
		
		f=Matrix([[0 for i in range(x.c)] for j in range(self.r)])
		
		if self.c==x.r:
			for i in range(self.r):
				for j in range(x.c):
					for k in range(x.c):
						f.a[i][j]+=(self.a[i][k])*x.a[k][j]
						
		return f		
					
		 
	
	
	def printl(self):
		print (self.a)
		
				
'''m1=Matrix([[1,2],[3,4],[5,6]])
m2=Matrix([[5,6],[3,4],[1,2]])
m3=Matrix([[1,1],[1,1],[1,1]])
m4 = m1+m2+m3
print (m4.a)
print(m1.a)
print(m2.a)
print(m3.a)
m5=Matrix([[1,0,0],[0,1,0],[0,0,1]])
m6=Matrix ([[1,2,3],[4,5,6],[7,8,9]])
m7=m5*m6
print(m7.a)
		'''
# Heap Sort		
class Heap:
	def __init__(self,a):
	        self.a=a
	        self.b=a
	def parent(self,i):
		return (i-1)//2
	def left (self,i):
		return (2*i+1)
	def right (self,i):
		return (2*i+2)

	def maxheap(self,i):
		l=self.left(i)
		r=self.right(i)
		lar=i
		if l<len(self.a) and self.a[i]< self.a[l]:
			lar=l
		if r<len(self.a) and self.a[lar]<self.a[r]:
			lar=r
		if lar != i:
			self.a[i],self.a[lar]=self.a[lar],self.a[i]
		self.maxheap(lar)
		
	def build_maxheap(self):
		for i in range ((len(self.b)//2)-1,-1,-1):
			self.maxheap(i)
			
			
				
				
o=Heap([2,4,5,1,8,0,1])
o.build_maxheap()
print(o.a)
		
		
		
		
