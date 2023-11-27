'''
    linked-list
        - is basically a data structure for storing 
        collection of items

    class Box {
        int data
        Box next
    }

    - it has 2 attributes or fields in this class
        - data/item
        box

    head.data
        - the data-head that the first box contain

    box next
        - reflects to the next bost that's connected to a 
        particular box.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = "- >")
            current = current.next
        print("None")

#Create a linked_list = LinkedList() and insert the input values

my_linked_list = LinkedList()
for value in input_values:
    my_linked_list.insert(value)

#Display the linked list
my_linked_list.display()

'''
    Mini-Activity
        - create a new file name it
        linkedlist_activity.py
        inside the discussion folder

        create a python program that will 
        simulate the linked list to form the name "LINUS TORVALDS" using 
        this input values
            [S, L, T, O, R, N, S, U, D, L, A, V]

'''



