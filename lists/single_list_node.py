from abc import ABC, abstractmethod
from nodes import SingleListNode
from exceptions import EmptyListException, InvalidPositionException, NoSuchElementException

class Lista(ABC):
    def __init__(self):
        self.start_node=None

    # Returns true iff the list contains no elements.
    def is_empty(self):
        if self.start_node==None:
            return True
        else:
            return False
    # Returns the number of elements in the list.
    def size(self):
        count=0
        n=self.start_node
        while n is not None:
            count+=1
            n=n.next_node
        return count


    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        if self.start_node==None:
            raise EmptyListException
        else:
            return self.start_node.element

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if self.start_node==None:
            raise EmptyListException
        else:
            n=self.start_node
            while n.next_node is not None:
                n=n.next_node
            print(n.element)

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        n=self.start_node
        count=0
        while n.next_node is not None:
            if count==position:
                return n.element
            n=n.next_node
            count+=1
        if count==position:
            return n.element
        else:
            raise InvalidPositionException

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        n=self.start_node
        count=0
        while n.next_node is not None:
            if n.element==element:
                return count
            count+=1
            n=n.next_node
        if n.element==element:
            return count
        else:
            return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node=SingleListNode(element)
        new_node.next_node=self.start_node
        self.start_node=new_node


    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new_node=SingleListNode(element)
        if self.start_node==None:
            self.start_node=new_node
            return
        else:
            n=self.start_node
            while n.next_node is not None:
                n=n.next_node
            n.next_node=new_node
    

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        new_node=SingleListNode(element)
        if position==0:
            new_node.next_node=self.start_node
            self.start_node=new_node
            return
        count=0
        n=self.start_node
        previous_node=0
        while n.next_node is not None:
            if count==position:
                previous_node.next_node=new_node
                new_node.next_node=n
                n=new_node
                return 
            count+=1
            previous_node=n
            n=n.next_node
        if count==position:
            n=self.start_node
            while n.next_node is not None:
                n=n.next_node
            n.next_node=new_node
        else:
            raise InvalidPositionException

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if self.start_node is None:
            raise EmptyListException
        else:
            self.start_node = self.start_node.next_node
            return self.start_node.element

    

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.start_node is None:
            raise EmptyListException
        else:
            n=self.start_node
            while n.next_node.next_node is not None:
                n=n.next_node
            n.next_node=None
            return n.element

    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        n=self.start_node
        previous_node=0
        count=0
        while n.next_node is not None:
            if count==position:
                previous_node.next_node=n.next_node
                return n.element
            previous_node=n
            n=n.next_node
            count+=1
        else:
            raise InvalidPositionException

    # Removes all elements from the list.
    def make_empty(self):
        self.start_node=None

        

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        if self.start_node is None:
            raise EmptyListException
        else:
            n=self.start_node
            while n is not None:
                print(n.element," ")
                n=n.next_node