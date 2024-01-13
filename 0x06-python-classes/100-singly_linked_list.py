#!/usr/bin/python3
"""Define a class of a SinglyLinkedList"""


class Node:
    """Define a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Constractor

        Args:
            data: the data that is contained in the node
            next_node: a pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property for the data in the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Property for the next_node instance"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a Singly_linked_list"""

    def __init__(self):
        """Constroctor"""

        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the list
        in an increasing order
        Args:
            value (node): the node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tp = self.__head
            while (tp.next_node is not None and
                    tp.next_node.data < value):
                tp = tp.next_node
            new.next_node = tp.next_node
            tp.next_node = new

    def __str__(self):
        """Define the Print() of the SinglyLinkedList"""

        values = []
        tp = self.__head
        while tp is not None:
            values.append(str(tp.data))
            tp = tp.next_node
        return ('\n'.join(values))
