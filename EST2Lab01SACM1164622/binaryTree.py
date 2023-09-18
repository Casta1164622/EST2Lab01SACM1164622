
class Node:
   def __init__(self, key,data):
      self.left = None
      self.right = None
      self.parent = None
      self.key = key
      self.data = data

   def insert(self, key,data):

      if self.key:
         if key < self.key:
            if self.left is None:
               self.left = Node(key, data)
               self.left.parent = self
            else:
               self.left.insert(key,data)
         elif key > self.key:
               if self.right is None:
                  self.right = Node(key,data)
                  self.right.parent = self
               else:
                  self.right.insert(key,data)
      else:
         self.key = key

   def searchDPI(root, search):
    currentNode = root 
    while(currentNode.key != search.key):
        if(int(search.key) == int(currentNode.key)):
            return currentNode
        elif(int(search.key) > int(currentNode.key)):
            currentNode = currentNode.right
            if currentNode == None:
                return None
        elif(int(search.key) < int(currentNode.key)):
            currentNode = currentNode.left
            if currentNode == None:
                return None
        elif(currentNode.left == None and currentNode.right == None):
            return None
    return currentNode


   def findParent(self, kidNode):
     currentNode = self
     if kidNode == None:
         return None
     if currentNode.left == None or currentNode.right == None:
         return currentNode
     while(currentNode.left!= kidNode and currentNode.right!= kidNode):

         if(currentNode.left == kidNode or currentNode.right == kidNode):
             return currentNode

         elif(kidNode.key['dpi'] > currentNode.key['dpi']):
             currentNode = currentNode.right
         elif(kidNode.key['dpi'] < currentNode.key['dpi']):
             currentNode = currentNode.left
         elif(currentNode.left == None and currentNode.right == None):
             return None
     if currentNode.left!= kidNode or currentNode.right!= kidNode:
         return currentNode
        

   def delete(self, deletingKey):
     nodeToDelete = Node.searchDPI(self, deletingKey)
     if nodeToDelete == None:
         return
     parent = nodeToDelete.parent
     nodeToDelete.parent = None
     #Si el nodo a borrar no tiene hijos
     if nodeToDelete.left == None and nodeToDelete.right == None:
         if parent.left == nodeToDelete:
             parent.left = None
         if parent.right == nodeToDelete:
             parent.right = None

     #Si el nodo solo tiene hijo izquierdo
     elif nodeToDelete.left != None and nodeToDelete.right == None:
         if parent.left == None:
             parent.right = nodeToDelete.left
         elif parent.right == None:
             parent.left = nodeToDelete.left
     #Si el nodo solo tiene un hijo derecho
     elif nodeToDelete.left == None and nodeToDelete.right != None:
         if parent.left == None:
             parent.right = nodeToDelete.right
         elif parent.right == None:
             parent.left = nodeToDelete.right
     #Si el nodo tiene dos hijos
     elif nodeToDelete.left != None and nodeToDelete.right != None:
         #Obtenemos el valor mas pequeño de lado derecho
         if nodeToDelete.left.left == None and nodeToDelete.left.right == None:
             temp = nodeToDelete.left
             nodeToDelete.data = temp.data
             nodeToDelete.left = None
         elif nodeToDelete.right.left == None and nodeToDelete.right.right == None:
             temp = nodeToDelete.right
             nodeToDelete.data = temp.data
             nodeToDelete.right = None
         else:
             subNode = nodeToDelete.right
             if subNode.left == None:
                 nodeToDelete.data = subNode
                 nodeToDelete.right = subNode.right
             else:
                while subNode.left != None:
                  subNode = subNode.left
                parentN = Node.findParent(self,subNode)
                nodeToDelete.data = subNode.data
                if(parentN.left == subNode):
                    parentN.left = None
                elif(parentN.right == subNode):
                    parentN.right = None
         
   def buscarNombres(self, nombre):
       res = []
       if not self:
           return res
       stack = []
       curr_node = self
       while curr_node or stack:
           while curr_node:
               stack.append(curr_node)
               curr_node = curr_node.left
           curr_node = stack.pop()
           if curr_node.data['name'] == nombre:
               res.append(curr_node.data)
           curr_node = curr_node.right
       return res





