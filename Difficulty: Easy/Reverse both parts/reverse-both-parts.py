
from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        # code here
        if not head or k == 0:
            return head
        
        curr = head
        Next = None
        prev = None
        while k:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            k -= 1
            
        p1 = prev
        curr = curr
        Next = None
        prev = None
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        
        temp = p1
        while temp.next:
            temp = temp.next
        temp.next = prev
        return p1
        
    

#{ 
 # Driver Code Starts

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()
def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        head = inputList()
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.reverse(head, k)
        
        printList(res)
        

# } Driver Code Ends