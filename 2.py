#!/usr/bin/python3
import random
from cmath import pi,exp

		
# 1.ordinary multiplication 2. Multiplication using FFT Assume both polynomial has same power
def ordinary(a,b):
	la,lb=len(a),len(b)
	
	n=la+lb-1
	c=[0 for x in range(n)]
	for i in range(la):
		for j in range(lb):
			c[i+j]+=a[i]*b[j]
	return c
			
	
a=[1,2]
b=[0,3]
#print (ordinary(a,b))

class poly:
	def __init__(self,a):
		x=a
		n=len(x)-1
	def nthroots(self,z):
		c=2j*pi/self.z
		cp1=[]
		cp= [exp(k * c) for k in range(self.z)]
		for i,j in enumerate(cp):
			img=j.imag
			if abs(j.imag)<0.000001:
				img=0.0
			y=complex(j.real,img)
			cp1.append(y)
		return cp1
#print(nthroots(2))	
pol1=poly([1,2])
pol2=poly([2,1])


# ASSUME n IS EVEN
	def FFT(self,a,w);
		if w==1.0+0j:
			return a

		A_even=[a[i] for i in range(0,len(a),2)]
		A_odd=[a[i] for i in range(1,len(a),2)]
		even=[FFT(A_even,w**2) for i in range(0,len(a),2)]
		odd=[[FFT(A_odd,w**2) for i in range(0,len(a),2)]			
		for j in range(0,len(a)/2):
			r[j]=even[j]+(w**j)*odd[j]
			r[j+len(a)/2]=even[j]-(w**j)*odd[j]	
		return r
		
	def multiply(x,y):
		
			
		
		
		

				
