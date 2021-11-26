# Convertendo uma lista duplamente ligada para lista circular dupla
class Node:
    def __init__(self, _data):
        self.data = _data
        self.nxt = None
        self.prev = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_type = 'linked'

    
    def append(self, _data):
        new_node = Node(_data)
        
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.convert_linked_circular(self.list_type)
    
    
    def convert_linked_circular(self, _type):
        self.list_type = _type
        
        if self.list_type == 'linked':
            self.head.prev = None
            self.tail.nxt = None
        elif self.list_type == 'circular':
            self.head.prev = self.tail
            self.tail.nxt = self.head
    
    
    def print_list(self):
        list_info = f'Lista tipo: {self.list_type} \n'
        aux = self.head
        
        if self.list_type == 'circular':
            list_info += '... '
        
        while aux:
            if aux.prev == None:
                list_info += f'<- {aux.data} <-> '
                print(f'Nó: {aux}\nValor: {aux.data}\nNó anterior: {None}\nPróximo nó: {aux.nxt.data}\n')
            elif aux.nxt == None:
                list_info += f'{aux.data} -> '
                print(f'Nó: {aux}\nValor: {aux.data}\nNó anterior: {aux.prev.data}\nPróximo nó: {None}\n')
            else:
                list_info += f'{aux.data} <-> '
                print(f'Nó: {aux}\nValor: {aux.data}\nNó anterior: {aux.prev.data}\nPróximo nó: {aux.nxt.data}\n')
            aux = aux.nxt
        
            if self.list_type == 'circular':
                if aux == self.head:
                    list_info += '...'
                    break
        
        print(list_info + '\n')


list1 = Linked_List()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

list1.convert_linked_circular('circular')
list1.print_list()

list1.append(47)
list1.print_list()

list1.convert_linked_circular('linked')
list1.append(58)
list1.print_list()
