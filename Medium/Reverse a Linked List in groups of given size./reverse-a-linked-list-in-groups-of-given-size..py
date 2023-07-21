"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self, head, k):
        if head is None:
            return None
        
        prev_group_tail = None
        new_head = None
        curr = head
        
        while curr:
            group_head = curr
            prev = None
            i = 0
            
            # Reverse the current group of k nodes
            while curr and i < k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                i += 1
            
            # Set the new head of the linked list if not set already
            if new_head is None:
                new_head = prev
            
            # Connect the reversed group with the previous reversed group
            if prev_group_tail:
                prev_group_tail.next = prev
            
            # Update the previous group tail for the next iteration
            prev_group_tail = group_head
        
        return new_head

#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends