class TreeObj:
    def __init__(self, indx, value=None):
        """
        :param indx: проверяемый в вершине дерева индекс вектора x;
        :param value: value - значение, хранящееся в вершине (принимает значение None для вершин, у которых есть потомки - промежуточных вершин)
        """
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    def has_descendants(self):
        return bool(self.left and self.right)


class DecisionTree:
    def __init__(self):
        pass

    @classmethod
    def predict(cls, root: TreeObj, x: list):
        next, i = root, 0
        while next.has_descendants():
            if x[i]:
                next = next.left
            else:
                next = next.right
            i = next.indx
        return next.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True) -> TreeObj:
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x =  [0, 1, 0]
x =  [0, 0, 0]
res = DecisionTree.predict(root, x)
print(res)