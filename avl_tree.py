from typing import override

from Trees import BinarySearchTree, Node


class AVLSearchTree[T](BinarySearchTree):

    @override
    def insert(self, data: T):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert(self.root, data)
        self._size += 1

    @override
    def _insert(self, node: Node, data: T) -> Node[T]:
        if node is None:
            return Node(data)

        if self.key(data) < self.key(node.data):
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        return self._balance(node)

    def _rotate_left(self, x: Node[T]) -> Node[T]:
        y = x.right
        z = y.left

        y.left = x
        x.right = z

        return y

    def _rotate_right(self, x: Node[T]) -> Node[T]:
        y = x.left
        z = y.right

        y.right = x
        x.left = z

        return y


    def _balance(self, node:Node[T]) -> Node[T]:
        balance_factor = self._get_balance(node)

        if balance_factor > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        if balance_factor < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)

            return self._rotate_left(node)

    def _get_balance(self, node: Node[T]) -> int:
        if node is None:
            return 0

        return self.height(node.left) - self.height(node.right)

    def height(self, node:Node[T])->int:
        if node is None:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))