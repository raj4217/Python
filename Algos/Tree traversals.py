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

    def preorder(self):
        print(self.key)
        if self.leftch:
            self.leftch.preorder()
        if self.rightch:
            self.rightch.preorder()

    def postorder(self):
        if self.leftch:
            self.leftch.postorder()
        if self.rightch:
            self.rightch.postorder()
        print(self.key)

    def inorder(self):
        if self.leftch:
            self.leftch.inorder()
        print(self.key)
        if self.rightch:
            self.rightch.inorder()


r = BinaryTree('a')
r.insrtLeft('b')
r.insrtRight('c')
r.getLeftch().insrtLeft('d')
r.getLeftch().insrtRight('e')
r.getRightch().insrtLeft('f')
r.getRightch().insrtRight('g')

r.preorder()
r.inorder()
r.postorder()
