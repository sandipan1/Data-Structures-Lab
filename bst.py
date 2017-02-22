class Node:
		def __init__(self,data):
			self.left=None
			self.right=None
			self.data=data
			self.parent=None
			self.mark=None


class Tree:

	
	def __init__(self):
		self.root=None


	def insert (self,num):
		start=Node(-1)
		if self.root is None:
			self.root=Node(num)
			self.root.parent=start
			self.root.mark='d'

		else:
			cur=self.root

			while 1:
				if num < cur.data:
					if cur.left:
						cur=cur.left
						#print cur.data,cur.mark,self.root.data
					else:
						cur.left=Node(num)
						cur.left.parent=cur
						cur.left.mark='l'
						break;
				elif num>cur.data:
					if cur.right:
						cur=cur.right
						#print cur.data, cur.mark,self.root.data
					else:
						cur.right=Node(num)
						cur.right.parent=cur
						cur.right.mark='r'
						break
				else:
					break


	def preorder( self,nd):
		if nd is not None:
			print nd.data,nd.mark,nd.parent.data
			self.preorder(nd.left)
			self.preorder(nd.right)


	def inorder( self,nd):
		if nd is not None:
			
			self.inorder(nd.left)
			print (nd.data,'-->',nd.parent.data)
			self.inorder(nd.right)

	# def transplant(self,u,v):
	# 	if u.parent is None:
	# 		self.root=v
	# 	elif u==u.parent.left:
	# 		u.parent.left=v
	# 	else u.parent.right=v
	# 	if v ==None:
	# 		v.parent=u.parent
	# def delete(	):



	def find(self,val):
		
		cur=self.root
		while 1:
			if cur.data == val:
				print 'found'
				return cur
				
				break
			elif val < cur.data:
					
				if cur.left:
					
					cur=cur.left

				else:	
					print 'not found'
					return None
					break
			elif val >cur.data:
				
				if cur.right:
					cur=cur.right
				else:
					print 'not found'
					return None
					break
	def min_node_subtree(self,node):
		while 1:
			if node.left:
				node=node.left
			else: return node
	def max_node_subtree(self,node):
		while 1:
			if node.right:
				node=node.right
			else: return node

	def predecessor(self,val):
		c=self.find(val)
		
		if c.left:
			return (self.max_node_subtree(c.left).data)
			
		else:
			while 1:
				if c.parent and c.mark=='r':
					return c.parent.data
					k=True
					break
				elif c.parent and c.mark=='l':
					c=c.parent
				else:
					return 'NO PREDECESSOR'
					break
			


	def successor(self,val):
		c=self.find(val)
		
		if c.right:
			return self.min_node_subtree(c.right).data
			
		else :
			while 1:
				if c.parent and c.mark=='l':
					return c.parent.data
					break
				elif c.parent and c.mark=='r':
					c=c.parent
				else:
					return "NO SUCCESSOR"


	def remove(self,val):
		c=self.find(val)
		if c is None :
			return (val+' not found')
		else :
			# no child
			if c.left is None and c.right is None:
				if c.mark=='l':
					c.parent.left=None
				elif c.mark=='r':
					c.parent.right=None
				else c.data=None

			# one child
			elif c.left is None and c.right:
				if c.mark=='l':
					c.parent.left=c.right
				elif c.mark=='r':
					c.parent.right=c.right

			elif c.left  and c.right is None:
				if c.mark=='l':
					c.parent.left=c.left
				elif c.mark=='r':
					c.parent.right=c.left

			#2 children



   def remove_rishabh(self,val) :
     if self is None :
       return False
    #a) data is in the root
     elif self.value == val :
       if self.LeftChild is None and self.RightChild is None :
         self.root = None
       elif self.LeftChild and self.RightChild is None :
         self = self.LeftChild
       elif self.RightChild and self.LeftChild is None :
         self= self.RightChild
       elif self.LeftChild and self.RightChild :
          delnodeparent = self
          delnode = self.RightChild
          while delnode.LeftChild :
            delnodeparent = delnode
            delnode = delnode.LeftChild
          self.value = delnode.value
      
          if delnode.RightChild :
            if delnodeparent.value > delnode.value:
              delnodeparent.LeftChild = delnode.RightChild
            else :
              delnodeparent.RightChild = delnode.RightChild
          else :
            if delnodeparent.value >delnode.value :
              delnodeparent.LeftChild = None
            else :
              delnodeparent.RightChild =None
    # b)data is not in the root
     parent = None
     node = self
    
     while node and node.value != val :
      parent = node
      if node.value < val :
         node = node.RightChild
      else :
        node = node.LeftChild
     #Case1 : Data not found
     if node is None or node.value != val :
      return False
   
     #Case2:node has no children
     elif node.LeftChild is None and node.RightChild is None :
      if parent.value > val :
        parent.LeftChild = None
      else :
        parent.RightChild = None

    #Case3:Node has left child only
     elif node.LeftChild and node.RightChild is None :
      if parent.value > val :
         parent.LeftChild = node.LeftChild
      elif parent.value < val :
         parent.RightChild = node.leftChild
    
    #Case4:Node has right child only
     elif node.RightChild and node.LeftChild is None :
      if parent.value > val :
         parent.LeftChild = node.RightChild
      elif parent.value< val :
         parent.RightChild = node.RightChild

    #Case5 : NOde has both left child and right child
     else :
      delnodeparent = node
      delnode = node.RightChild
      while delnode.LeftChild :
        delnodeparent = delnode
        delnode = delnode.LeftChild
      node.value = delnode.value
      
      if delnode.RightChild :
        if delnodeparent.value > delnode.value:
            delnodeparent.LeftChild = delnode.RightChild
        else :
            delnodeparent.RightChild = delnode.RightChild
      else :
         if delnodeparent.value >delnode.value :
            delnodeparent.LeftChild = None
         else :
            delnodeparent.RightChild =None
 





	

tree=Tree()
ar=[5,525,4,17,32,0,3]

for i in ar:
	tree.insert(i)
tree.preorder(tree.root)
#print(tree.max_node_subtree(tree.root).data)

print (tree.predecessor(0))
print (tree.successor(525))
