# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
	def __init__(self, L = None):
		super().__init__(L)

	def rearrange(self):
		initial_head = self.head
		node = self.head
		min = node.next_node.value
		while node.next_node:
			if min > node.next_node.value:
				min = node.next_node.value
				self.head = node
			node = node.next_node
		while node.next_node:
			node = node.next_node
		node.next_node = initial_head
		while node.next_node != self.head:
			node = node.next_node
		node.next_node = None
		second_item = self.head
		# above is step 2, choose the number in front of the smallest as the head.
		# >>> 49, 97, 53, 5, 33, 65
		# >>> 53, 5, 33, 65, 49, 97
		
		even_node = self.head
		odd_node = self.head.next_node
		begin_even = even_node
		begin_odd = odd_node
		while True:
			if even_node.next_node and even_node.next_node.next_node:
				even_node.next_node = even_node.next_node.next_node
				even_node = even_node.next_node
			else:
				break
			if odd_node.next_node and odd_node.next_node.next_node:
				odd_node.next_node = odd_node.next_node.next_node
				odd_node = odd_node.next_node
			else:
				break
		odd_node.next_node = begin_even
		even_node.next_node = None
		self.head = begin_odd
		# above is step 3, rearranged from step 2, by the sequence of 2,4,6,...,1,3,5,...
		# >>> 53, 5, 33, 65, 49, 97
		# >>> 5, 65, 97, 53, 33, 49
		
		while self.head.next_node != second_item:
			even_node = self.head
			odd_node = self.head.next_node
			begin_even = even_node
			begin_odd = odd_node
			while True:
				if even_node.next_node and even_node.next_node.next_node:
					even_node.next_node = even_node.next_node.next_node
					even_node = even_node.next_node
				else:
					break
				if odd_node.next_node and odd_node.next_node.next_node:
					odd_node.next_node = odd_node.next_node.next_node
					odd_node = odd_node.next_node
				else:
					break
			even_node.next_node = begin_odd
			odd_node.next_node = None
		# above is step 4, rearranged from step 3, use sequence of 1,3,5,...,2,4,6,...
		# untill we get the final answer
		
		# end !
		
        # Replace pass above with your code
    
    
    
