from linkedlist import LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    #prepends data at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    #append data at last
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    #prints the data of entire list
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    #removes a node of given key
    # A -> B -> C -> D ->....
    #Remove key = "B"
    # A -> C -> D ->....
    def remove(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.NEXT
                    cur = cur.next

    #counts the number of nodes in the list
    def __len__(self): # overwrting the keyword len
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    #splits list from half
    #A -> B -> c  -> D -> ...
    #A -> B -> ... and C -> D -> ...
    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("\n")
        split_cllist.print_list()

    #removes the given node
    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    #Josephus problem
    def josephus_circle(self,step):
        cur = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("REMOVED: " + str(cur.data))
            self.remove_node(cur)
            cur = cur.next

    #to check if the provided list is Circular Linked List or not
    def is_circular_linked_list(self, input_list):
        cur = input_list.head

        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False
