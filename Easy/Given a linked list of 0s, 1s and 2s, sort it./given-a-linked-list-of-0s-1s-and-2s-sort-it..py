#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        if not head or not head.next:
            return head

    # Create dummy nodes for the three lists
        dummy_0 = Node(0)
        dummy_1 = Node(0)
        dummy_2 = Node(0)
    
        # Create pointers for the three lists
        zero_ptr = dummy_0
        one_ptr = dummy_1
        two_ptr = dummy_2
    
        current = head
    
        # Traverse the original linked list
        while current:
            if current.data == 0:
                zero_ptr.next = current
                zero_ptr = zero_ptr.next
            elif current.data == 1:
                one_ptr.next = current
                one_ptr = one_ptr.next
            else:
                two_ptr.next = current
                two_ptr = two_ptr.next
    
            current = current.next
    
        # Connect the three lists
        zero_ptr.next = dummy_1.next if dummy_1.next else dummy_2.next
        one_ptr.next = dummy_2.next
        two_ptr.next = None
    
        # Update the head of the linked list
        head = dummy_0.next
    
        return head
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print()

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        printList(Solution().segregate(a.head))
# } Driver Code Ends