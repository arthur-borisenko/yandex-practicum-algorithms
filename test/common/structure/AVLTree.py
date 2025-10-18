import unittest
from main.common.structure.AVLTree import AVLTree


class TestCase(unittest.TestCase):
    @classmethod
    def _dfs(cls, node):
        if node.right is not None and node.left is not None:
            return cls._dfs(node.left) + [node.value] + cls._dfs(node.right)
        elif node.left is not None:
            return cls._dfs(node.left) + [node.value]
        elif node.right is not None:
            return [node.value] + cls._dfs(node.right)
        else:
            return [node.value]

    def test_add(self):
        test_tree = AVLTree()
        test_data = [1, 6, 3, 4, 21, 12, 43]
        for value in test_data:
            test_tree.insert(value)
        self.assertEqual(self._dfs(test_tree.root), sorted(self._dfs(test_tree.root)))

    def test_add_illegal_value(self):
        test_tree = AVLTree()
        test_data = [1, 6, 3, 4, 21, 12, 6, 43]
        try:
            for value in test_data:
                test_tree.insert(value)
            self.assertFalse(True, "error is not raised on already added node")
        except ValueError:
            self.assertTrue(True)

    @classmethod
    def _check_height_single(cls, node):
        return (
            node.height
            == max(
                node.left.height if node.left is not None else 0,
                node.right.height if node.right is not None else 0,
            )
            + 1
        )

    @classmethod
    def _check_height(cls, node):
        if node.right is not None and node.left is not None:
            return (
                cls._check_height(node.right)
                and cls._check_height(node.left)
                and cls._check_height_single(node)
            )
        elif node.left is not None:
            return cls._check_height(node.left) and cls._check_height_single(node)
        elif node.right is not None:
            return cls._check_height(node.right) and cls._check_height_single(node)
        else:
            return cls._check_height_single(node)

    def test_height(self):
        test_tree = AVLTree()
        self.DEBUG = test_tree
        test_data = [1, 6, 3, 4, 21, 12, 43]
        for value in test_data:
            test_tree.insert(value)
            r = self._check_height(test_tree.root)
            assert r
