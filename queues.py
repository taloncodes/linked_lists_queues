class Node:  # create class to enable Nodes to be added to the LL
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self, newhead=None):
        self.head = newhead
        self.tail = None

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setHead(self, newhead):
        self.head = newhead

    def setTail(self, newtail):
        self.tail = newtail

    # add an item to the list.
    # Complexity is O(1) as the value to add is passed directly into the list.
    # as the value can be stored dynamically in memory, the algorithm does not need to loop through each item in the
    # list
    def addItem(self, item):
        newNode = Node(item)  # create new node object
        newNode.setNext(self.head)  # set next item to current head of list
        self.head = newNode  # set new item as new head item of list

    # remove an item from the list
    # Complexity is O(n) as the algorithm must loop (n) times in order to find the item to delete.
    def removeItem(self, item):
        current = self.head  # current node to check if item is a match, starts at head
        previous = None  # Previous node to set new pointer
        found = False
        while not found:  # loop until found
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()  # change next value of previous node

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # find the size of the list
    # Complexity is O(n) as the algorithm must loop (n) times to increment the counter
    def findSize(self):
        current = self.head
        count = 0
        while current != None:  # finish loop when current is None, as this denotes the end of the LL
            count += 1  # increment counter for each entry
            current = current.getNext()
        return count

    # check if an item is in the list
    # Complexity is O(n) as the algorithm must loop (n) times to evaluate every element in the list
    def checkItem(self, item):
        current = self.head  # assign current variable to head of list
        found = False  # Boolean value to return, indicating whether or not the value has been found
        while current != None and found == False:  # while not at end of list and item not found, iterate through list
            if current.getData() == item:  # if found, return true
                found = True
            else:
                current = current.getNext()

        return found


ll = LinkedList()

print(ll.findSize())

ll.addItem(1)
print(ll.checkItem(1))

print(ll.findSize())

ll.removeItem(1)
print(ll.checkItem(1))

print(ll.findSize())
