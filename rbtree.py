import time
import random 
import math
import cmath

class node :
  def __init__(self,k,l=None,r=None,p=None,c=None) :
     self.value = k
     self.left=None
     self.right= None
     self.parent = None
     self.color = 'B'

class redblacktree :
  def __init__(self):
     self.root = None

  def leftrotate(self,x) :
     y=x.right
     x.right = y.left
     if y.left :
       y.left.parent = x
     
     y.parent = x.parent
     
     if x.parent is None :
       self.root = y
     elif x.parent.left == x :
       x.parent.left = y
     else :
       x.parent.right = y
     
     y.left = x
     x.parent = y
 
  def rightrotate(self,x) :
     y = x.left
     x.left = y.right
     if y.right :
       y.right.parent = x
     y.parent = x.parent
     if x.parent == None :
       self.root = y
     elif x.parent.left == x :
       x.parent.left = y
     else :
       x.parent.right = y
     y.right = x
     x.parent = y

  def insert(self,k) :
    if self.root == None :
       self.root = node(k)
    
    else :
      x = self.root
      while(x != None) :
        y=x
        if x.value > k:
          x=x.left
          var = 'l'
        elif x.value <k :
          x=x.right
          var = 'r'
        
      if var =='r' :
         y.right = node(k)
         y.right.parent = y
         z=y.right
         z.color = 'R'
      else :
         y.left = node(k)
         y.left.parent = y
         z=y.left
         z.color = 'R'

      if z.parent.color == 'R' :
         self.insert_fixup(z)
   
  def uncle(self,z):
      p=z.parent
      g=z.parent.parent
      if g.left == p :
        return g.right
      elif g.right == p :
        return g.left


  def insert_fixup(self,z):
      y = self.uncle(z)
      if y!= None:
        if y.color == 'R' :
         while(z.parent.color == 'R'):
           z.parent.color = 'B'
           self.uncle(z).color = 'B'
           z.parent.parent.color = 'R'
           z = z.parent.parent
        
        else :
           if z.parent.parent.left == z.parent :
              if z.parent.left == z :
                  g=z.parent.parent
                  self.rightrotate(g)
                  g.color = 'R'
                  g.parent.color = 'B'
         
              else :
                  p=z.parent
                  g=z.parent.parent
                  self.leftrotate(p)
                  self.rightrotate(g)
                  g.color = 'R'
                  g.parent.color = 'B'
 
           else :
              if z.parent.right == z :
                  g=z.parent.parent
                  self.leftrotate(g)
                  g.color = 'R'
                  g.parent.color = 'B'
         
              else :
                  p=z.parent
                  g=z.parent.parent
                  self.rightrotate(p)
                  self.leftrotate(g)
                  g.color = 'R'
                  g.parent.color = 'B'

  def transplant(self,u,v) :
      if u.parent == None :
          self.root = v
      elif u.parent.left == u :
          u.parent.left = v
      else :
          u.parent.right = v
      v.parent = u.parent

  def minimum(self,x):
		
		while x.left!=None:
			x=x.left
		return x

  def deletion(self,z):
     
		if z.left==None:
			self.transplant(z,z.right)
		elif z.right==None:
			self.transplant(z,z.left)
		else:
			y=self.minimum(z.right)
			if y.parent!=z:
				self.transplant(y,y.right)
				y.right=z.right
				y.right.parent=y

			self.transplant(z,y)
			y.left=z.left
			y.left.parent=y
  


  '''def inorder_traversal(self,x):
		if x.right!=None and x.left!=None:
			self.inorder_traversal(x.left)
			print(x.value)
			self.inorder_traversal(x.right)
		elif x.right!=None:
			
			print(x.value)
			self.inorder_traversal(x.right)
		elif x.left!=None:
			self.inorder_traversal(x.left)
			print(x.value)
			
			
		else:
			print(x.value)
  '''
  def in_order(self,x) :
      if x :
        if x.left :
           self.in_order(x.left)
        print(str(x.value))
        if x.right :
           self.in_order(x.right) 


		
  def printing(self):
		self.in_order(self.root)

      #self.inorder_traversal(self.root)

               
  #def delete(self,z) :
 
a=[1,5,6,2,8,3]
p= redblacktree()
for k in range(len(a)):
  p.insert(a[k])

p.printing()
#p.deletion(node(8))
#p.printing()
Chat Conversation End
