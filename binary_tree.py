class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    # endmethod

    def output(self, order: str):
        if order == "pre":
            print(self.value)
            if self.left:
                self.left.output(order)
            if self.right:
                self.right.output(order)
        elif order == "in":
            if self.left:
                self.left.output(order)
            print(self.value)
            if self.right:         
                self.right.output(order)
        elif order == "post":
            if self.left:
                self.left.output(order)
            if self.right:
                self.right.output(order)
            print(self.value)
        else:   
            raise ValueError(f"Unknown Order: {order}")
    # endmethod
    

    def search(self, target) -> bool:
        if self.value == target:
            return True
        elif (self.left != None) and (self.left.search(target)):
            return True
        elif (self.right != None) and (self.right.search(target)):
            return True
        return False
    # endmethod
# endclass