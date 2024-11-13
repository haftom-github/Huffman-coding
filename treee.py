class Tree():
    class Node():
        def __init__(self, item, weight):
            self.item = item                            #holds character          will be None except in the leafs of the huffman tree
            self.weight = weight                        #holds the weight of the character
            self.left = None
            self.right = None

    def __init__(self, item, weight):
        self.head = self.Node(item, weight)

    def concat(self, subtree, to):                      #concatinates a tree as a left or right child
        if to == 'left':
            self.head.left = subtree.head
            return  self
        if to == 'right':
            self.head.right = subtree.head
        return self

    def getweight(self):
        return self.head.weight