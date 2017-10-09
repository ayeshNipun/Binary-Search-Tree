class node:
  def __init__(self, d, l=None, r=None, p=None):
    self.data = d
    self.left = l
    self.right = r
    self.parent = p
    
  def getData(self):
    return self.data
    
  def setData(self,d):
    self.data = d
    
class BST:
  def __init__(self,rt=None):
    self.root = rt
    
  def add(self, d):
    if self.root == None:
      self.root = node(d)
      print(d,"Added as Root..")
    else:
      cur = self.root
      new = node(d)
      while True:
        if cur.data > d:
          if cur.left == None:
            cur.left = new
            new.parent = cur
            print(d,"Added as Left Child of",cur.data)
            return
          else:
            cur = cur.left
        else:
          if cur.right == None:
            cur.right = new
            new.parent = cur
            print(d,"Added as right Child of",cur.data)
            return
          else:
            cur = cur.right
  
  def search(self, d):
    cur = self.root
    while cur != None:
      if cur.data == d:
        return (cur)
      elif cur.data > d:
        cur = cur.left
      else:
        cur = cur.right
    return False
  
  def isLeaf(self, nd):
    if nd.left == None and nd.right == None:
      return True
    else:
      return False
      
  def side(self, nd):
    if nd.data < self.root.data:
      return ("left")
    else:
      return ("right")
      
  def identy(self, d):
    nd = self.search(d)
    if nd.data < self.root.data:
      if nd.right == None:
        return ("ll")
      elif nd.left == None:
        return ("lr")
      else:
        return ("lp")
    else:
      if nd.right == None:
        return ("rl")
      elif nd.left == None:
        return ("rr")
      else:
        return ("rp")
      
  def delete(self, d):
    cur = self.search(d)
    if cur == False:
      print(d,"is not in the tree..")
    else:
      if self.isLeaf(cur):
        if self.side(cur) == "left":
          cur.parent.left = None
          cur.parent = None
          print(d,"is deleted...")
        else:
          cur.parent.righ = None
          cur.parent = None
          print(d,"is deleted")
      elif self.identy(cur) == "ll":
        cur.parent.left = cur.left
        cur = None
      elif self.identy(cur) == "lr":
        cur.parent.left = cur.right
        cur = None
      elif self.identy(cur) == "lp":
        cur.right.left = cur.left
        cur.left = None
        cur.parent.left = cur.right
        cur = None
      elif self.identy(cur) == "rr":
        cur.parent.right = cur.right
        cur = None
      elif cur.identy(cur) == "rl":
        cur.parent.right = cur.left
        cur = None
      #else:
       # cur.
        
  def inorder(self):
    def trav(root):
      if root != None:
        trav(root.left)
        print(root.data)
        trav(root.right)
    trav(self.root)
    
  def preorder(self):
    def trav(root):
      if root != None:
        print(root.data)
        trav(root.left)
        trav(root.right)
    trav(self.root)
    
  def postorder(self):
    def trav(root):
      if root != None:
        trav(root.left)
        trav(root.right)
        print(root.data)
    trav(self.root)
  
  
t = BST()

t.add(20)
t.add(15)
t.add(30)
t.add(16)
t.add(25)
t.add(12)
t.add(35)

t.delete(12)   
t.delete(17)

print("\n\n\n-------------------------")
print("----Inorder Traversal----")
t.inorder()

print("\n\n--------------------------")
print("----Preorder Traversal----")
t.preorder()

print("\n\n---------------------------")
print("----Postorder Traversal----")
t.postorder()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            