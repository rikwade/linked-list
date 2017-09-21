'''
Simple Doubly Linked List class implementation in Python
Richard Wade (rik@rikwade.com)
'''

class element:
    ''' Define the list element object
    '''
    prev = None
    next = None
    data = None

    def __init__(self, value):
        self.prev = None
        self.next = None
        self.data = value

    def dump(self):
        return self.data

class linkedList:
    ''' Define the Linked List object and its methods
    '''
    head = None
    tail = None
    len = 0

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def length(self):
        # function to return the length of the list
        return self.len

    def add(self, value):
        # function to create a new list element, populated with a value
        newElement = element(value)
        newElement.prev = self.tail

        if newElement.prev != None:
            newElement.prev.next = newElement

        newElement.next = None

        self.tail = newElement
        if self.len == 0:
            self.head = newElement
        self.len += 1

    def delete(self, llist, delEle):
        # function to delete an element from the list
        if delEle.prev:
            delEle.prev.next = delEle.next
        else:
            llist.head = delEle.next
        if delEle.next:
            delEle.next.prev = delEle.prev
        else:
            llist.tail = delEle.prev

    def search(self, value):
        # function to search the list for a value and return the element object
        searchEle = self.head
        while searchEle != None:
            if searchEle.data == value:
                return searchEle
            searchEle = searchEle.next

        return None

    def dump(self):
        # function to dump the values of the list
        dumpEle = self.head
        while dumpEle != None:
            print(dumpEle.data)
            dumpEle = dumpEle.next

if __name__ == '__main__':
    myList = linkedList()
    print("Length: ", myList.length())
    myList.add('a')
    print("Length: ", myList.length())
    print("Head Dump: ", myList.head.dump())
    print("Tail Dump: ", myList.tail.dump())
    myList.add('b')
    print("Length: ", myList.length())
    print("Head Dump: ", myList.head.dump())
    print("Tail Dump: ", myList.tail.dump())
    ele = myList.search('a')
    print("Element Dump: ", ele.dump())
    print("Dumping List before delete:")
    myList.dump()
    myList.delete(myList, ele)
    print("Dumping List after delete:")
    myList.dump()

