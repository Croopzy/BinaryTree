class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, valueIn):
        if (valueIn < self.value):
            if self.left:
                self.left.insert(valueIn)
            else:
                self.left = TreeNode(valueIn)
        else:
            if self.right:
                self.right.insert(valueIn)
            else:
                self.right = TreeNode(valueIn)

    def output(self, order: str):
        if order == "pre":
            print(self.value, end = " ")
            if self.left:
                self.left.output(order)
            if self.right:
                self.right.output(order)
        elif order == "in":
            if self.left:
                self.left.output(order)
            print(self.value, end = " ")
            if self.right:         
                self.right.output(order)
        elif order == "post":
            if self.left:
                self.left.output(order)
            if self.right:
                self.right.output(order)
            print(self.value, end = " ")
        else:   
            raise ValueError(f"Unknown Order: {order}")

    def search(self, target) -> bool:
        if self.value == target: return True
        if self.left and (self.left.search(target)): return True
        if self.right and (self.right.search(target)): return True
        return False

    def max_depth(self) -> int:
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def copy(self):
        newtree = TreeNode(self.value)
        newtree.left = self.left.copy() if self.left else None
        newtree.right = self.right.copy() if self.right else None
        return newtree
# endclass