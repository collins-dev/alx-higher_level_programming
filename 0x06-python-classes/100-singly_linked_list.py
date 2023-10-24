#!/usr/bin/python3
<<<<<<< HEAD


class Node:
    """Node of a singly linked list.
    Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def next_node(self, value)
    Instantiation with data and next_node.
    """

    def __init__(self, data, next_node=None):
        """Initializes the data of the node."""
=======
""" defines a class node and singlylinkedlist"""


class Node:
    """defines the node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes the node"""
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
<<<<<<< HEAD
        """Retrieves the data from the node."""
=======
        """retrieves the data"""
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
        return self.__data

    @data.setter
    def data(self, value):
<<<<<<< HEAD
        """Sets the data into a node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node."""
=======
        """sets the data"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """gets the next node"""
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
<<<<<<< HEAD
        """Sets the next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list.
    Private instance attribute: head.
    Simple instantiation.
    Public instance method: def sorted_insert(self, value).
    """

    def __init__(self):
        """Initializes the linked list."""
        self.head = None

    def __str__(self):
        """For the print statement in the main file."""
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
=======
        """ets the next node"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts node in the correct order"""
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data
                    < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """defines the print representation of the list"""
        tmp = self.__head
        values = []
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
>>>>>>> b734e1e857971cc40fedee1a42d5c8e4b50ece53
