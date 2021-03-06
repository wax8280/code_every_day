# coding:utf-8
'''
对于一棵由黑白点组成的二叉树，我们需要找到其中最长的单色简单路径，其中简单路径的定义是从树上的某点开始沿树边走不重复的点到树上的另一点结束而形成的路径，而路径的长度就是经过的点的数量(包括起点和终点)。而这里我们所说的单色路径自然就是只经过一种颜色的点的路径。你需要找到这棵树上最长的单色路径。

给定一棵二叉树的根节点(树的点数小于等于300，请做到O(n)的复杂度)，请返回最长单色路径的长度。这里的节点颜色由点上的权值表示，权值为1的是黑点，为0的是白点。
'''


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# TREE = Node(0,
#             Node(1, Node(1), Node(0)),
#             Node(0, Node(0), Node(1))
#             )

TREE = Node(0,
            Node(1, Node(0, Node(1, Node(1))), Node(0)),
            Node(1, Node(0), Node(0))
            )


def func(root):
    B_res, W_res = [], []

    def res(root, W, B):
        if root == None:
            B_res.append(B)
            W_res.append(W)
            return
        if root.val == 0:
            W += 1
            B_res.append(B)
            B = 0
        elif root.val == 1:
            B += 1
            W_res.append(W)
            W = 0
        res(root.left, W, B)
        res(root.right, W, B)

    res(root, 0, 0)
    return max(max(B_res), max(W_res))

