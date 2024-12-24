class DLLNode:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self, *initial_data):
        """ Initializes a new doubly linked list with the given initial_data."""
        self.length = 0
        if len(initial_data) == 0:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            for data in initial_data:
                self.append(data)
                
    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise.
        :return bool:
        """
        return self.length == 0
    
    def find(self, data) -> DLLNode | None:
        """Find the first node containing the given data.
        :param Any data: The data to search for.
        :return DLLNode | None: The first node containing the given data, or None if the data is not found.
        """
        node = self.head
        
        while node is not None:
            if node.data == data: return node
            node = node.next
            
        return None
    
    def append(self, *data) -> int:
        """Appends the given data to the end of the list.
        :return int: The new length of the list.
        """
        for d in data:    
            if self.is_empty():
                self.head = DLLNode(d)
                self.tail = self.head
            else:
                new_node = DLLNode(d, self.tail, None)
                self.tail.next = new_node
                self.tail = new_node
            
        self.length += len(data)
        return self.length
    
    def prepend(self, *data) -> int:
        """Prepends the given data to the beginning of the list.
        :return int: The new length of the list.
        """
        for d in data:
            if self.is_empty():
                self.head = DLLNode(d)
                self.tail = self.head
            else:
                new_node = DLLNode(d, None, self.head)
                self.head.prev = new_node
                self.head = new_node
                
        self.length += len(data)
        return self.length
    
    def items(self) -> list:
        """Returns a list of all the items in the Linked List.
        :return list:
        """
        data = list()
        if self.is_empty(): return data
        
        node = self.head
        while node is not None:
            data.append(node.data)
            node = node.next
            
        return data
        
