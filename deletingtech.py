class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head

        
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

       
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def delete_at_position(self, position):
        if self.head is None:
            return

        temp = self.head

        
        if position == 0:
            self.head = temp.next
            temp = None
            return

      
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        
        if temp is None:
            return
        if temp.next is None:
            return

        
        next = temp.next.next

        
        temp.next = None
        temp.next = next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


if _name_ == "_main_":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    
    print("Created linked list:")
    llist.print_list()
    
    llist.delete_node(3)
    print("\nLinked list after deleting node with data 3:")
    llist.print_list()
    
    llist.delete_at_position(1)
    print("\nLinked list after deleting node at position 1:")
    llist.print_list()