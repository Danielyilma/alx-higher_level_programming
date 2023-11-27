class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    head = None
    def __init__(self):
        pass

    def sorted_insert(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            seted = False
            prev = None
            while temp is not None:
                if value < temp.data:
                    newnode.next_node = temp

                    if prev is None:
                        self.head = newnode
                    else:
                        prev.next_node = newnode
                    seted = True
                    break
                prev = temp
                temp = temp.next_node

            if not seted:
                temp.next_node = newnode
            
    
    def __str__(self):
        if self.head is not None:
            temp = self.head
            result = ""
            while (temp is not None):
                result += str(temp.data)
                temp = temp.next_node
                if temp:
                    result += "\n"
            return result