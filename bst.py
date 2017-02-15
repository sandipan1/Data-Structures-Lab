class Node:
		def __init__(self,data):
			self.left=None
			self.right=None
			self.data=data
			self.parent=None


class Tree:

	
	def __init__(self):
		self.root=None


	def insert (self,num):
		if self.root is None:
			self.root=Node(num)
		else:
			cur=self.root

			while 1:
				if num < cur.data:
					if cur.left:
						cur=cur.left
					else:
						cur.left=Node(num)
						break;
				elif num>cur.data:
					if cur.right:
						cur=cur.right
					else:
						cur.right=Node(num)
				else:
					break


	def preorder( self,nd):
		if nd is not None:
			print nd.data
			self.preorder(nd.left)
			self.preorder(nd.right)


	def inorder( self,nd):
		if nd is not None:
			
			self.inorder(nd.left)
			print nd.data
			self.inorder(nd.right)

	def transplant(self,u,v):
		if u.parent is None:
			self.root=v
		elif u==u.parent.left:
			u.parent.left=v
		else u.parent.right=v
		if v ==None:
			v.parent=u.parent
	def delete(	)

tree=Tree()
ar=[1,2,4,5,8,0,7]
for i in ar:
	tree.insert(i)
tree.inorder(tree.root)



