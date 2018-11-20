# Written by Jiaquan for COMP9021


from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
	def __init__(self):
		super().__init__()

	def insert(self, value):
		if self.value == None:
			self.value = value
			self.left_node = BinaryTree()
			self.right_node = BinaryTree()
			return
		node = self
		new_position = self.size() + 1
		levels = int(log(new_position, 2))
		parent_nodes = [node]
		level_begin = 2 ** levels
		level_nodes = level_begin
		for i in range(levels-1):
			## means new_position are in the left part of this subtree, then start with 
			## left_node as root, and record this root in parent_nodes list.
			level_nodes = level_nodes // 2
			if new_position < level_begin + level_nodes:
				node = node.left_node
			else:
				node = node.right_node
				level_begin = level_begin + level_nodes
			parent_nodes.append(node)
		if new_position == level_begin:
			node.left_node = BinaryTree(value)
			new_node = node.left_node
		else:
			node.right_node = BinaryTree(value)
			new_node = node.right_node
		for i in (len(parent_nodes)-1, 0, -1):
			father = parent_nodes[i]
			if new_node.value < father.value:
				new_node.value, father.value = father.value, new_node.value
				
				
				
				
				
				
				
		# Replace pass above with your code
