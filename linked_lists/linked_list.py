class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None   # empty list starts with no head

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
           self.head = new_node
        else:
           current=self.head
           while current.next is not None:
              current=current.next
           current.next=new_node

    def search(self,target):
        current=self.head
        while current is not None:
              if current.data==target:
                 return True
              else:
                  current=current.next
        return False
    
    def delete(self,target):
        if self.head is None:
           return
        if self.head.data==target:
           self.head=self.head.next
           return
        previous=self.head
        current=self.head.next
        while current is not None: 
            if current.data==target:
                previous.next=current.next
                return 
            previous=current
            current=current.next
  
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# test
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(25)
ll.insert_at_end(7)
ll.print_list()  # expected: 10 -> 25 -> 7 -> None
print(ll.search(25))  # expected: True
print(ll.search(99))  # expected: False
ll.delete(25)
ll.print_list()  # expected: 10 -> 7 -> None