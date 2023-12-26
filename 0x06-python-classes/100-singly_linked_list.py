#!/usr/bin/python3
"""
A class node that creates a linked list
"""
class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.

    Methods:
        data(self): Getter method to retrieve the data stored in the node.
        data(self, value): Setter method to set the data stored in the node.
        next_node(self): Getter method to retrieve the next node in the linked list.
        next_node(self, value): Setter method to set the next node in the linked list.
        __init__(self, data, next_node=None): Initializes a new instance of the Node class.
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data stored in the node.

        Args:
            None

        Returns:
            The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the linked list.

        Args:
            None

        Returns:
            The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Returns:
            None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        __head (Node): The head node of the linked list.

    Methods:
        __init__(self): Initializes a new instance of the SinglyLinkedList class.
        sorted_insert(self, value): Inserts a new Node into the correct sorted position in the list (increasing order).
        __str__(self): Returns a string representation of the linked list.
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be stored in the new Node.

        Returns:
            None
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Args:
            None

        Returns:
            A string representation of the linked list.
        """
        current = self.__head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
