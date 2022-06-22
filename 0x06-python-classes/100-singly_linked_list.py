#!/usr/bin/python3
"""
This module contains two classes Node and SinglyLinkedList
Node is used to make nodes
Singlylinkedlist for a single linked list
"""


class Node:
    """
    Node class for creating a node
    each node has data and next node
    Attributes:
            next
            data
    """

    def __init__(self, data, next_node=None):
        """
        Used to initialise a node
        Data then next_node
        """
        if type(data) != int:
            raise TypeError("data must be an integer")
        elif not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object2")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def next_node(self):
        """
        next_node getter. Used to get next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    @property
    def data(self):
        """
        Used to retrieve data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Used to change the data
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value


class SinglyLinkedList:
    """
    Class Singlylinkedlist
    head and other attributes
    """

    def __init__(self):
        """
        Private instance attribute: head (no setter or getter)
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node to a linked list
        the nodes are arranged according to data
        """
        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
            return
        current = self.__head
        if(newNode.data < current.data):
            newNode.next_node = current
            self.__head = newNode
            return
        while (current.next_node):
            next1 = current.next_node
            if(newNode.data < next1.data):
                newNode.next_node = next1
                current.next_node = newNode
                return
            current = current.next_node
        current.next_node = newNode

    def __str__(self):
        """
        for printing the class in order
        """
        mystr = ""
        current = self.__head
        while(current):
            mystr += str(current.data)
            mystr += '\n'
            current = current.next_node
        return mystr[:-1]
