class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftch = None
        self.rightch = None

    def insrtLeft(self, newNode):
        if not self.leftch:
            self.leftch = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftch = self.leftch
            self.leftch = temp

    def insrtRight(self, newNode):
        if not self.rightch:
            self.rightch = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightch = self.rightch
            self.leftch = temp

    def getRightch(self):
        return self.rightch

    def getLeftch(self):
        return self.leftch

    def setRootval(self, val):
        self.key = val

    def getRootval(self):
        return self.key
